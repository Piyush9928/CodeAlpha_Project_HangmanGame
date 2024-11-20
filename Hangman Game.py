import tkinter as tk
from tkinter import messagebox
import random

# Word list
WORDS = ["python", "programming", "hangman", "developer", "keyboard", "algorithm"]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.word_to_guess = random.choice(WORDS)
        self.guessed_word = ["_"] * len(self.word_to_guess)
        self.guessed_letters = set()
        self.attempts = 6

        # GUI Layout
        self.label_word = tk.Label(root, text="Word to Guess: " + " ".join(self.guessed_word), font=("Helvetica", 16))
        self.label_word.pack(pady=10)

        self.label_attempts = tk.Label(root, text=f"Attempts Left: {self.attempts}", font=("Helvetica", 14))
        self.label_attempts.pack(pady=10)

        self.entry_guess = tk.Entry(root, font=("Helvetica", 14))
        self.entry_guess.pack(pady=10)

        self.button_guess = tk.Button(root, text="Guess", command=self.guess_letter, font=("Helvetica", 14))
        self.button_guess.pack(pady=10)

    def guess_letter(self):
        guess = self.entry_guess.get().lower()
        self.entry_guess.delete(0, tk.END)

        # Validate input
        if not guess.isalpha() or len(guess) != 1:
            messagebox.showerror("Invalid Input", "Please enter a single letter.")
            return
        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", f"You've already guessed '{guess}'.")
            return

        self.guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in self.word_to_guess:
            for i, letter in enumerate(self.word_to_guess):
                if letter == guess:
                    self.guessed_word[i] = guess
            self.label_word.config(text="Word to Guess: " + " ".join(self.guessed_word))

            # Check for win
            if "_" not in self.guessed_word:
                messagebox.showinfo("Congratulations", f"You've guessed the word: {self.word_to_guess}!")
                self.reset_game()
        else:
            self.attempts -= 1
            self.label_attempts.config(text=f"Attempts Left: {self.attempts}")
            if self.attempts == 0:
                messagebox.showerror("Game Over", f"You're out of attempts! The word was: {self.word_to_guess}")
                self.reset_game()

    def reset_game(self):
        self.word_to_guess = random.choice(WORDS)
        self.guessed_word = ["_"] * len(self.word_to_guess)
        self.guessed_letters = set()
        self.attempts = 6
        self.label_word.config(text="Word to Guess: " + " ".join(self.guessed_word))
        self.label_attempts.config(text=f"Attempts Left: {self.attempts}")

# Create the main window
root = tk.Tk()
game = HangmanGame(root)
root.mainloop()
