from env.environment import ITSupportEnv
from env.models import Action


class Client:
    def __init__(self):
        self.env = ITSupportEnv()

    def reset(self):
        return self.env.reset().dict()

    def step(self, action: dict):
        act = Action(**action)
        obs, reward, done, info = self.env.step(act)

        return {
            "observation": obs.dict(),
            "reward": reward,
            "done": done,
            "info": info
        }
