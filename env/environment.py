import random
from env.models import Observation, Action, State
from env.tasks import TASKS
from env.reward import calculate_reward


class ITSupportEnv:
    def __init__(self):
        self.state = None
        self.current_task = None

    # Reset environment (start new problem)
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
        reward = calculate_reward(
            action.action_type,
            action.content,
            self.current_task["solution"]
        )

        # Save history
        self.state.history.append(f"{action.action_type}: {action.content}")

        # Check if solved
        if action.action_type == "resolve" and reward > 0:
            self.state.solved = True

        done = self.state.solved

        observation = Observation(
            problem=self.state.problem,
            history=self.state.history,
            status="resolved" if done else "ongoing"
        )

        return observation, reward, done, {}

    # Return current state
    def state(self):
        return self.state