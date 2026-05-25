from number_generator import generate_target
from input_validator import get_valid_input
from hint_generator import get_hint
from scorer import calculate_score


def play_game():
    min_val, max_val = 1, 100
    target_number = generate_target(min_val, max_val)
    attempts = 0
    guessed_correctly = False

    print(f"--- Welcome to the Number Guesser ---")
    print(f"I'm thinking of a number between {min_val} and {max_val}.")

    while not guessed_correctly:
        attempts += 1
        guess = get_valid_input(
            f"Attempt {attempts} - Your guess: ", min_val, max_val)

        hint = get_hint(guess, target_number)
        print(hint)

        if guess == target_number:
            guessed_correctly = True

    final_score = calculate_score(attempts)
    print(f"\nCongratulations! You found the number in {attempts} attempts.")
    print(f"Your final score is: {final_score}/100")


if __name__ == "__main__":
    play_game()
