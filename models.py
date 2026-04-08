from pydantic import BaseModel
from typing import List


class Observation(BaseModel):
    problem: str
    history: List[str]
    status: str


class Action(BaseModel):
    action_type: str
    content: str


class Reward(BaseModel):
    score: float
