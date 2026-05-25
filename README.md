# Number Guesser Pro

A clean, modular Python implementation of the classic Number Guesser game, featuring a sleek desktop GUI and persistent high scores.

## 🚀 Features

- **Graphical User Interface:** Modern, dark-themed desktop app built with Tkinter.
- **Leaderboard System:** Persistent Top 5 high scores saved locally via JSON.
- **Modular Architecture:** Strict separation of concerns (scoring, validation, GUI, generation).
- **Standalone Executable:** Ready to be compiled into a single `.exe` or Linux binary using PyInstaller.
- **Error Handling:** Robust input validation to prevent unexpected crashes.

## 📁 Project Structure

```text
NUMBER_GUESSER/
├── hint_generator.py        # Logic for high/low/warm/cold hints
├── leaderboard_manager.py   # Handles saving/loading JSON high scores
├── main_gui.py              # Main desktop application and GUI loop
├── number_generator.py      # Target number creation
├── scorer.py                # Point calculation logic
└── leaderboard.json         # Auto-generated file storing player records
```
