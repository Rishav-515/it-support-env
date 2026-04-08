def grade_task(history, solution):
    score = 0

    for action in history:
        if solution.lower() in action.lower():
            score += 1

    raw_score = score / max(len(history), 1)

    # 🚨 Clamp strictly between (0, 1)
    if raw_score <= 0:
        return 0.01
    elif raw_score >= 1:
        return 0.99
    else:
        return raw_score