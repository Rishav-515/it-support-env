---
title: it-support-env
sdk: docker
---
# IT Support RL Environment

This project implements a reinforcement learning-style environment for IT support troubleshooting. The system simulates how an agent interacts with a user by asking questions and suggesting fixes to resolve technical issues.

---

## Features

- Custom environment with:
  - State tracking (problem, history, status)
  - Action handling (ask_question, suggest_fix)
  - Reward system based on relevance
  - Episode lifecycle management
- FastAPI backend for interaction
- Deployed on Hugging Face Spaces

---

## Environment Design

### State
- problem: User issue
- history: List of actions taken
- status: ongoing / resolved

### Actions
- ask_question -> gather more information  
- suggest_fix -> propose a solution  

### Reward Logic
- Relevant actions -> positive reward  
- Irrelevant or repeated actions â†’ penalty  

---

## API Endpoints

- GET / -> Health check  
- POST /reset -> Reset environment  
- POST /step -> Take action  

---

## Demo

Run locally:

```bash
python demo.py
```

---

## Live Demo

https://huggingface.co/spaces/Rishav-515/it-support-env

---

## API Documentation

https://rishav-515-it-support-env.hf.space/docs

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Project Structure

env/                # Core environment logic (state, tasks, reward, graders)
server/             # FastAPI backend for interaction
inference.py        # LLM-powered agent execution script
demo.py             # Local testing script
client.py           # API interaction client
Dockerfile          # Deployment configuration
requirements.txt    # Dependencies
README.md           # Project documentation

---

## Design Highlights

- Reinforcement learning-style interaction loop
- Task-specific graders for contextual evaluation
- Dynamic reward shaping to guide agent behavior
- LLM-driven decision making for adaptive troubleshooting

## Key Strength

Unlike rule-based systems, this environment:
- adapts actions based on problem context
- penalizes incorrect troubleshooting paths
- simulates real-world IT support workflows

## Future Improvements

- Fine-tuned policy model for action selection
- Feedback-driven reward optimization
- Multi-turn conversational memory enhancement


## Authors

- Rishav Raj
- Raunak Raj