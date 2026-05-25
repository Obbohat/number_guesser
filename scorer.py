def calculate_score(attempts: int, max_score: int = 100, penalty_per_guess: int = 10) -> int:
    """Calculates the final score. Prevents score from dropping below 0."""
    score = max_score - ((attempts - 1) * penalty_per_guess)
    return max(0, score)
