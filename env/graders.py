def grade_task(history, solution):
    score = 0

    for action in history:
        if solution.lower() in action.lower():
            score += 1

    return score / max(len(history), 1)