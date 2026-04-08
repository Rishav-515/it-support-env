import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
from typing import List

from openai import OpenAI

from env.environment import ITSupportEnv
from env.models import Action
from env.graders import grade_task


# ===== ENV CONFIG =====
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
HF_TOKEN = os.getenv("HF_TOKEN")   # FIXED (no fallback)

# REQUIRED CHECK (for compliance)
if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

MAX_STEPS = 6


# ===== LOGGING (STRICT FORMAT) =====
def log_start(task: str, env: str, model: str):
    print(f"[START] task={task} env={env} model={model}", flush=True)


def log_step(step: int, action: str, reward: float, done: bool, error=None):
    error_val = error if error else "null"
    done_val = str(done).lower()
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={done_val} error={error_val}",
        flush=True,
    )


def log_end(success: bool, steps: int, score: float, rewards: List[float]):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}",
        flush=True,
    )


# ===== SIMPLE AGENT =====
def get_action(client, problem, history):
    prompt = f"""
You are an IT support assistant.

Problem:
{problem}

History:
{history}

Choose ONE action:
- ask_question
- suggest_fix
- resolve

Respond in format:
action_type|content
"""

    try:
        res = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=100,
        )
        text = res.choices[0].message.content.strip()

        if "|" in text:
            action_type, content = text.split("|", 1)
        else:
            action_type, content = "ask_question", text

        return Action(action_type=action_type.strip(), content=content.strip())

    except Exception:
        return Action(action_type="ask_question", content="Can you provide more details?")


# ===== MAIN LOOP =====
def main():
    
    client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

    env = ITSupportEnv()
    observation = env.reset()

    rewards = []
    history = []
    steps_taken = 0

    log_start(task="it_support", env="it_support_env", model=MODEL_NAME)

    done = False

    for step in range(1, MAX_STEPS + 1):
        if done:
            break

        action = get_action(client, observation.problem, observation.history)

        observation, reward, done, _ = env.step(action)

        rewards.append(reward)
        history = observation.history
        steps_taken = step

        log_step(step, f"{action.action_type}:{action.content}", reward, done)


    score = grade_task(history, env.current_task["solution"])
    success = score >= 0.5

    log_end(success, steps_taken, score, rewards)


if __name__ == "__main__":
    main()
