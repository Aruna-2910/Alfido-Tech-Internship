import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("400x250")
        self.secret_number = random.randint(1,100)
        self.attempts = 0
        self.max_attempts = 10
        self.label = tk.Label(master,text="Guess a number between 1 and 100", font=("Arial",12))
        self.label.pack(pady=10)
        self.entry = tk.Entry(master,font=("Arial",14))
        self.entry.pack(pady=5)
        self.button = tk.Button(master,text="Submit Guess",command=self.check_guess)
        self.button.pack(pady=5)
        self.attempt_label = tk.Label(master, text=f"Attempts left:{self.max_attempts}",font=("Arial",12))
        self.attempt_label.pack(pady=5)
        self.hint_label = tk.Label(master, text="",font=("Arial",12), fg="blue")
        self.hint_label.pack(pady=5)

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            messagebox.showwarning("Invalid Input","please enter a valid number!")
            return
        guess = int(guess)
        self.attempts += 1
        attempts_left = self.max_attempts - self.attempts
        self.attempt_label.config(text=f"Attempts left: {attempts_left}")
        if guess < self.secret_number:
            self.hint_label.config(text="Too low!")
        elif guess > self.secret_number:
            self.hint_label.config(text="Too high!")
        else:
            messagebox.showinfo("Congratulations",f"you guessed it in {self.attempts} attempts!")
            self.restart_game()
            return
        if self.attempts >= self.max_attempts:
            messagebox.showinfo("Game over", f"you've used all attempts! The number was {self.secret_number}")
            self.restart_game()

    def restart_game(self):
        self.secret_number = random.randint(1,100)
        self.attempts = 0
        self.entry.delete(0,tk.END)
        self.hint_label.config(text="")
        self.attempt_label.config(text=f"Attempts left: {self.max_attempts}")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
            
