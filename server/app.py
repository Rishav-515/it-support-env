from fastapi import FastAPI
from env.environment import ITSupportEnv
from env.models import Action
import uvicorn
import os

app = FastAPI()

# Initialize environment
env = ITSupportEnv()


# ROOT ROUTE (fixes "Starting..." issue)
@app.get("/")
def root():
    return {
        "message": "IT Support API is running",
        "docs": "/docs"
    }


# RESET ENDPOINT
@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()


# STEP ENDPOINT
@app.post("/step")
def step(action: dict):
    act = Action(**action)
    obs, reward, done, info = env.step(act)

    return {
        "observation": obs.dict(),
        "reward": reward,
        "done": done,
        "info": info
    }


# IMPORTANT: Dynamic port for Hugging Face
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run("server.app:app", host="0.0.0.0", port=port)