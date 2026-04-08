from env.graders import grade_task

TASKS = [
    {
        "problem": "My internet is very slow",
        "solution": "restart router",
        "keywords": ["restart", "router", "modem"],
        "grader": grade_task
    },
    {
        "problem": "My laptop is overheating and shutting down",
        "solution": "clean fan",
        "keywords": ["fan", "clean", "cooling"],
        "grader": grade_task
    },
    {
        "problem": "My screen is flickering",
        "solution": "update drivers",
        "keywords": ["driver", "update", "graphics"],
        "grader": grade_task
    }
]