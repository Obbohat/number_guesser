def get_valid_input(prompt: str, min_val: int, max_val: int) -> int:
    """Prompts the user until a valid integer within the range is provided."""
    while True:
        user_input = input(prompt)
        try:
            guess = int(user_input)
            if min_val <= guess <= max_val:
                return guess
            else:
                print(
                    f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
