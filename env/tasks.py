from env.graders import grade_internet, grade_overheating, grade_screen

TASKS = [
    {
        "problem": "My internet is very slow",
        "solution": "restart router",
        "keywords": ["restart", "router", "modem"],
        "grader": grade_internet
    },
    {
        "problem": "My laptop is overheating and shutting down",
        "solution": "clean fan",
        "keywords": ["fan", "clean", "cooling"],
        "grader": grade_overheating
    },
    {
        "problem": "My screen is flickering",
        "solution": "update drivers",
        "keywords": ["driver", "update", "graphics"],
        "grader": grade_screen
    },
    {
        "problem": "My WiFi keeps disconnecting",
        "solution": "check router placement",
        "keywords": ["router", "signal", "placement"],
        "grader": grade_internet
    },
    {
        "problem": "My computer is very slow",
        "solution": "close background apps",
        "keywords": ["background", "apps", "performance"],
        "grader": grade_overheating
    }
]