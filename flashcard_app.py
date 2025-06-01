import tkinter as tk
from tkinter import PhotoImage
import pandas as pd
import random
import os

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT_PATH = "images/card_front.png"
CARD_BACK_PATH = "images/card_back.png"
WRONG_IMAGE_PATH = "images/wrong.png"
RIGHT_IMAGE_PATH = "images/right.png"
DATA_PATH = "data/french_words.csv"
TO_LEARN_PATH = "data/words_to_learn.csv"


# ---------------------------- FLASHCARD APP CLASS --------------------- #
class FlashCardApp:
    def __init__(self):
        self.current_word_pair = {}
        self.words_to_learn = self.load_data()

        # Setup window
        self.window = tk.Tk()
        self.window.title("Flash Cards")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        # Set flip timer
        self.flip_timer = self.window.after(3000, self.flip_card)

        # Load images
        self.card_front_image = PhotoImage(file=CARD_FRONT_PATH)
        self.card_back_image = PhotoImage(file=CARD_BACK_PATH)
        self.wrong_button_image = PhotoImage(file=WRONG_IMAGE_PATH)
        self.right_button_image = PhotoImage(file=RIGHT_IMAGE_PATH)

        # Create canvas and card elements
        self.canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.card_image_on_canvas = self.canvas.create_image(400, 263, image=self.card_front_image)
        self.card_title = self.canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
        self.canvas.grid(row=0, column=0, columnspan=2)

        # Create buttons
        self.wrong_button = tk.Button(image=self.wrong_button_image, highlightthickness=0, command=self.next_card)
        self.wrong_button.grid(row=1, column=0)

        self.right_button = tk.Button(image=self.right_button_image, highlightthickness=0, command=self.is_known)
        self.right_button.grid(row=1, column=1)

        # Start the app
        self.next_card()
        self.window.mainloop()

    # ---------------------------- DATA HANDLING ------------------------------- #
    def load_data(self):
        """Loads word list from file or creates new one if file doesn't exist."""
        try:
            data = pd.read_csv(TO_LEARN_PATH)
        except FileNotFoundError:
            data = pd.read_csv(DATA_PATH)
        return data.to_dict(orient="records")

    # ---------------------------- SHOW NEW CARD ------------------------------- #
    def next_card(self):
        """Picks a new card and resets the timer."""
        self.window.after_cancel(self.flip_timer)
        self.current_word_pair = random.choice(self.words_to_learn)
        self.canvas.itemconfig(self.card_title, text="French", fill="black")
        self.canvas.itemconfig(self.card_word, text=self.current_word_pair["French"], fill="black")
        self.canvas.itemconfig(self.card_image_on_canvas, image=self.card_front_image)
        self.flip_timer = self.window.after(3000, self.flip_card)

    # ---------------------------- FLIP CARD ----------------------------------- #
    def flip_card(self):
        """Reveals the English translation."""
        self.canvas.itemconfig(self.card_title, text="English", fill="white")
        self.canvas.itemconfig(self.card_word, text=self.current_word_pair["English"], fill="white")
        self.canvas.itemconfig(self.card_image_on_canvas, image=self.card_back_image)

    # ---------------------------- WORD KNOWN --------------------------------- #
    def is_known(self):
        """Removes known word and updates the to-learn list."""
        self.words_to_learn.remove(self.current_word_pair)
        new_data = pd.DataFrame(self.words_to_learn)
        new_data.to_csv(TO_LEARN_PATH, index=False)
        self.next_card()


# ---------------------------- RUN APP --------------------------------- #
if __name__ == "__main__":
    FlashCardApp()
