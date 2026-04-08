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

env/
server/
demo.py
requirements.txt
README.md

---

## Author

Rishav Raj
