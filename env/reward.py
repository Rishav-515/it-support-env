def compute_reward(action, task):
    content = action.content.lower()

    # Ask question (limit excessive questioning)
    if action.action_type == "ask_question":
        return 0.2 if len(content) > 5 else -0.1

    # Suggest fix (context aware)
    if action.action_type == "suggest_fix":
        for keyword in task["keywords"]:
            if keyword in content:
                return 0.6
        return -0.4   # stronger penalty for wrong fixes

    # Resolve action
    if action.action_type == "resolve":
        if task["solution"] in content:
            return 0.9   # avoid 1.0 (validator safe)
        return -0.5

    return -0.1