def get_hint(guess: int, target: int) -> str:
    """Returns a hint comparing the guess to the target."""
    difference = abs(guess - target)

    if guess == target:
        return "Spot on!"

    hint = "Too high!" if guess > target else "Too low!"

    # Optional: Add "temperature" to the hints
    if difference <= 5:
        hint += " (But you are burning hot!)"
    elif difference <= 15:
        hint += " (You are getting warm.)"

    return hint
