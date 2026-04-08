def grade_internet(history):
    score = sum("router" in h.lower() for h in history) / max(len(history), 1)
    return min(max(score, 0.01), 0.99)


def grade_overheating(history):
    score = sum("fan" in h.lower() or "cool" in h.lower() for h in history) / max(len(history), 1)
    return min(max(score, 0.01), 0.99)


def grade_screen(history):
    score = sum("driver" in h.lower() for h in history) / max(len(history), 1)
    return min(max(score, 0.01), 0.99)

def grade_task(history, solution):
    # fallback generic grader (validator expects this name)
    score = sum(solution.lower() in h.lower() for h in history) / max(len(history), 1)
    return min(max(score, 0.01), 0.99)