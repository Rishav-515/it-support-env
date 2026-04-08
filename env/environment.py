import random
from env.models import Observation, Action, State
from env.tasks import TASKS
from env.reward import compute_reward


class ITSupportEnv:
    def __init__(self):
        self.state = None
        self.current_task = None

    # Reset environment
    def reset(self):
        self.current_task = random.choice(TASKS)

        self.state = State(
            problem=self.current_task["problem"],
            history=[],
            solved=False
        )

        return Observation(
            problem=self.state.problem,
            history=self.state.history,
            status="ongoing"
        )

    # Take action
    def step(self, action: Action):
        reward = compute_reward(action, self.current_task)

        self.state.history.append(f"{action.action_type}: {action.content}")

        from env.graders import grade_task
        score = grade_task(self.state.history, self.current_task["solution"])

        if score > 0.8:
            self.state.solved = True

        done = self.state.solved

        observation = Observation(
            problem=self.state.problem,
            history=self.state.history,
            status="resolved" if done else "ongoing"
        )

        return observation, reward, done, {}