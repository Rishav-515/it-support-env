from pydantic import BaseModel
from typing import List


class Observation(BaseModel):
    problem: str
    history: List[str]
    status: str  # "ongoing" or "resolved"


class Action(BaseModel):
    action_type: str  # ask_question, suggest_fix, resolve, escalate
    content: str


class Reward(BaseModel):
    score: float


class State(BaseModel):
    problem: str
    history: List[str]
    solved: bool
