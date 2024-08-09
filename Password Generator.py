import tkinter as tk
from tkinter import messagebox
import random

def choose_word():
    words = ['python', 'hangman', 'programming', 'developer', 'function']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def update_display():
    display.set(display_word(word, guessed_letters))

def guess_letter():
    global incorrect_guesses
    guess = letter_entry.get().lower()
    letter_entry.delete(0, tk.END)
    
    if len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        return

    if guess in guessed_letters:
        messagebox.showinfo("Repeated Guess", "You've already guessed that letter.")
        return

    if guess in word:
        guessed_letters.add(guess)
        update_display()
        if all(letter in guessed_letters for letter in word):
            messagebox.showinfo("Congratulations", f"You've guessed the word: {word}")
            root.quit()
    else:
        incorrect_guesses += 1
        attempts_left.set(f"Attempts left: {max_incorrect_guesses - incorrect_guesses}")
        if incorrect_guesses >= max_incorrect_guesses:
            messagebox.showinfo("Game Over", f"The word was: {word}")
            root.quit()

root = tk.Tk()
root.title("Hangman Game")
root.configure(bg='red')  # Set background color to red

word = choose_word()
guessed_letters = set()
incorrect_guesses = 0
max_incorrect_guesses = 6

display = tk.StringVar()
display.set(display_word(word, guessed_letters))

attempts_left = tk.StringVar()
attempts_left.set(f"Attempts left: {max_incorrect_guesses - incorrect_guesses}")

tk.Label(root, textvariable=display, font=("Helvetica", 20), bg='red', fg='white').pack(pady=20)
tk.Label(root, textvariable=attempts_left, font=("Helvetica", 14), bg='red', fg='white').pack(pady=10)

letter_entry = tk.Entry(root, font=("Helvetica", 16))
letter_entry.pack(pady=10)
tk.Button(root, text="Guess", command=guess_letter, font=("Helvetica", 16)).pack(pady=10)

root.mainloop()