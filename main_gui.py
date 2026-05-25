import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from number_generator import generate_target
from hint_generator import get_hint
from scorer import calculate_score
from leaderboard_manager import load_leaderboard, save_score


class NumberGuesserGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Pro Number Guesser")
        self.root.geometry("450x550")
        self.root.resizable(False, False)

        # Game State
        self.min_val, self.max_val = 1, 100
        self.target_number = 0
        self.attempts = 0

        self.setup_styles()
        self.create_widgets()
        self.start_new_game()

    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        # Modern Dark-ish Theme Look
        self.root.configure(bg="#1e1e2e")
        self.style.configure("TLabel", background="#1e1e2e",
                             foreground="#cdd6f4", font=("Arial", 11))
        self.style.configure("Header.TLabel", font=(
            "Arial", 16, "bold"), foreground="#89b4fa")
        self.style.configure("Hint.TLabel", font=(
            "Arial", 12, "italic"), foreground="#fab387")
        self.style.configure("TButton", font=(
            "Arial", 10, "bold"), background="#89b4fa", foreground="#11111b")
        self.style.map("TButton", background=[("active", "#b4befe")])

    def create_widgets(self):
        # Header
        ttk.Label(self.root, text="🎯 Number Guesser Pro",
                  style="Header.TLabel").pack(pady=15)

        # Instructions
        self.instruction_lbl = ttk.Label(
            self.root, text=f"Guess the number between {self.min_val} and {self.max_val}")
        self.instruction_lbl.pack(pady=5)

        # Input Section
        input_frame = ttk.Frame(self.root, style="TFrame")
        self.style.configure("TFrame", background="#1e1e2e")
        input_frame.pack(pady=15)

        self.guess_entry = ttk.Entry(input_frame, font=(
            "Arial", 14), width=10, justify="center")
        self.guess_entry.pack(side=tk.LEFT, padx=5)
        self.guess_entry.bind("<Return>", lambda event: self.check_guess())

        self.submit_btn = ttk.Button(
            input_frame, text="Guess", command=self.check_guess)
        self.submit_btn.pack(side=tk.LEFT, padx=5)

        # Feedback/Hint Status
        self.hint_lbl = ttk.Label(
            self.root, text="Good Luck!", style="Hint.TLabel")
        self.hint_lbl.pack(pady=10)

        self.attempts_lbl = ttk.Label(self.root, text="Attempts: 0")
        self.attempts_lbl.pack(pady=5)

        # Leaderboard Area
        ttk.Label(self.root, text="🏆 Top Records", font=(
            "Arial", 12, "bold"), foreground="#a6e3a1").pack(pady=(20, 5))

        self.leaderboard_text = tk.Text(self.root, height=6, width=45, bg="#313244", fg="#cdd6f4", font=(
            "Courier", 10), bd=0, padx=10, pady=5)
        self.leaderboard_text.pack(pady=5)
        self.update_leaderboard_display()

        # Restart Button
        ttk.Button(self.root, text="Restart Game",
                   command=self.start_new_game).pack(pady=15)

    def start_new_game(self):
        self.target_number = generate_target(self.min_val, self.max_val)
        self.attempts = 0
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.config(state="normal")
        self.submit_btn.config(state="normal")
        self.hint_lbl.config(text="Enter a number to start!")
        self.attempts_lbl.config(text="Attempts: 0")

    def check_guess(self):
        raw_input = self.guess_entry.get()
        try:
            guess = int(raw_input)
            if not (self.min_val <= guess <= self.max_val):
                raise ValueError
        except ValueError:
            messagebox.showwarning(
                "Invalid Input", f"Please enter a valid integer between {self.min_val} and {self.max_val}.")
            return

        self.attempts += 1
        self.attempts_lbl.config(text=f"Attempts: {self.attempts}")

        hint = get_hint(guess, self.target_number)
        self.hint_lbl.config(text=hint)

        if guess == self.target_number:
            self.handle_win()

    def handle_win(self):
        self.guess_entry.config(state="disabled")
        self.submit_btn.config(state="disabled")
        final_score = calculate_score(self.attempts)
        
        # Prompt for Name if it makes the leaderboard
        player_name = simpledialog.askstring("Winner!", f"You got it in {self.attempts} tries!\nScore: {final_score}/100\nEnter name for leaderboard:")
        
        if player_name is not None:
            save_score(player_name, final_score, self.attempts)
            self.update_leaderboard_display()

    def update_leaderboard_display(self):
        self.leaderboard_text.config(state="normal")
        self.leaderboard_text.delete("1.0", tk.END)
        records = load_leaderboard()

        if not records:
            self.leaderboard_text.insert(
                tk.END, "\n      No records yet! Be the first! 😉")
        else:
            self.leaderboard_text.insert(
                tk.END, f"{'Rank':<6}{'Name':<20}{'Score':<10}{'Attempts'}\n")
            self.leaderboard_text.insert(tk.END, "-" * 45 + "\n")
            for idx, r in enumerate(records, 1):
                self.leaderboard_text.insert(
                    tk.END, f" #{idx:<3}{r['name'][:18]:<20}{r['score']:<10}{r['attempts']}\n")

        self.leaderboard_text.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuesserGUI(root)
    root.mainloop()
