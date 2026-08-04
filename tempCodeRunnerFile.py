import customtkinter as ctk
import main as game
# Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
# Window
app = ctk.CTk()
app.title("Guess the Number Game")
app.geometry("400x400")
# Title Label
title = ctk.CTkLabel(app, text="Guess the Number Game", font=("Arial", 20))
title.pack(pady=20)
# Subtitle Label
subtitle = ctk.CTkLabel(app, text="Guess a number between 1 and 100", font=("Arial", 14))
subtitle.pack(pady=10)
player_label = ctk.CTkLabel(app, text="Your Guess: ?")
player_label.pack(pady=5)
result_label = ctk.CTkLabel(app, text="Result: ?")
result_label.pack(pady=5)
attempts_label = ctk.CTkLabel(app, text="Attempts: 0")
attempts_label.pack(pady=5)
# Function
def make_guess():
    game.guess = int(entry.get())  # get text from entry box
    player_label.configure(text=f"Your Guess: {game.guess}")
    result_label.configure(text="Result: " + game.guess_number())
# Buttons
guess_button = ctk.CTkButton(app, text="Make Guess", command=make_guess)
guess_button.pack(pady=10)
entry = ctk.CTkEntry(app, placeholder_text="Enter your guess")
entry.pack(pady=10)



app.mainloop()