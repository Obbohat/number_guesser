import random

def generate_target(min_val: int = 1, max_val: int = 100) -> int:
    """Generates a random integer between min_val and max_val (inclusive)."""
    return random.randint(min_val, max_val)