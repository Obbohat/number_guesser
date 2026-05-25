import json
import os
from typing import List, Dict, Any

LEADERBOARD_FILE = "leaderboard.json"


def load_leaderboard() -> List[Dict[str, Any]]:
    """Loads the top scores from the JSON file."""
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    try:
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_score(player_name: str, score: int, attempts: int) -> List[Dict[str, Any]]:
    """Saves a new score and returns the updated Top 5 ranking."""
    leaderboard = load_leaderboard()

    # Append new record
    leaderboard.append({
        "name": player_name if player_name.strip() else "Anonymous",
        "score": score,
        "attempts": attempts
    })

    # Sort by score descending, then by attempts ascending
    leaderboard.sort(key=lambda x: (-x["score"], x["attempts"]))

    # Keep only top 5 records
    top_five = leaderboard[:5]

    try:
        with open(LEADERBOARD_FILE, "w") as f:
            json.dump(top_five, f, indent=4)
    except IOError:
        print("Warning: Could not save high score to disk.")

    return top_five
