def compute_reward(action, task):
    content = action.content.lower()

    if action.action_type == "ask_question":
        return 0.2

    if action.action_type == "suggest_fix":
        for keyword in task["keywords"]:
            if keyword in content:
                return 0.6
        return -0.2

    if action.action_type == "resolve":
        if task["solution"] in content:
            return 1.0
        return -0.5

    return 0