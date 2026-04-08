def grade_task(history, correct_solution):
    """
    history: list of actions taken
    correct_solution: expected solution string
    """

    correct_solution = correct_solution.lower()

    # Check if correct solution was ever used
    for step in history:
        if correct_solution in step.lower():
            return 1.0

    # Partial score if some effort was made
    if len(history) > 0:
        return 0.5

    return 0.0
