# Number Guesser Game

A clean, modular Python implementation of the classic Number Guesser game. 

## 🚀 Features
* **Modular Architecture:** Strict separation of concerns (scoring, validation, generation).
* **Type Hinting:** Fully typed for a better developer experience and code reliability.
* **Jupyter Integration:** Play interactively right from your notebook environment in VS Code.
* **Error Handling:** Robust input validation to prevent unexpected crashes.

## 📁 Project Structure
```text
NUMBER_GUESSER/
├── hint_generator.py      # Logic for high/low/warm/cold hints
├── input_validator.py     # Ensures robust user input handling
├── main.ipynb             # Interactive Jupyter entry point
├── main.py                # CLI entry point and game loop orchestration
├── number_generator.py    # Target number creation
└── scorer.py              # Point calculation logic