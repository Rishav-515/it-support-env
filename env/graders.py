def grade_internet(history, solution):
    score = sum("router" in h.lower() for h in history) / max(len(history), 1)
    return min(max(score, 0.01), 0.99)


def grade_overheating(history, solution):
    score = sum(
        ("fan" in h.lower() or "cool" in h.lower())
        for h in history
    ) / max(len(history), 1)
    return min(max(score, 0.01), 0.99)


def grade_screen(history, solution):
    score = sum("driver" in h.lower() for h in history) / max(len(history), 1)
    return min(max(score, 0.01), 0.99)


# REQUIRED for inference.py compatibility
def grade_task(history, solution):
    score = sum(solution.lower() in h.lower() for h in history) / max(len(history), 1)
    return min(max(score, 0.01), 0.99)