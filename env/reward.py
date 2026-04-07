def calculate_reward(action_type: str, content: str, correct_solution: str):
    content = content.lower()
    correct_solution = correct_solution.lower()

    # If AI resolves correctly
    if action_type == "resolve" and correct_solution in content:
        return 1.0

    # If AI suggests correct fix (partial reward)
    if action_type == "suggest_fix" and correct_solution in content:
        return 0.6

    # If AI asks a question (small reward)
    if action_type == "ask_question":
        return 0.2

    # Wrong or useless action
    return -0.2