# 🧠 Flashcard Language Learning App

Learn French the smart way! This is a **flashcard app** built with Python using **Tkinter** and **Pandas** to help you memorize vocabulary through a visual, interactive experience.

---

## 🚀 Features

- 🎴 Flashcard interface for French–English vocabulary
- ⏳ Automatic card flipping after 3 seconds
- ✅ Marks known words and removes them from future practice
- 💾 Saves your progress automatically to `words_to_learn.csv`
- 🌙 Clean, user-friendly interface with images and animations

---

## 📸 Screenshots

> *(Add a screenshot or screen recording here if you can)*

---

## 🧰 Built With

- [Python 3.x](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) – GUI framework
- [Pandas](https://pandas.pydata.org/) – CSV file management

---

## 🗂 Folder Structure

flashcard-app/
├── data/
│ ├── french_words.csv # Main word dataset
│ └── words_to_learn.csv # Updated as you progress
├── images/
│ ├── card_front.png
│ ├── card_back.png
│ ├── right.png
│ └── wrong.png
├── flashcard_app.py # Python main script
└── README.md # This file

---

## 💻 How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/<your-username>/flashcard-app.git
cd flashcard-app

pip install pandas

python flashcard_app.py

📝 How It Works
A French word is shown first.

After 3 seconds, the card flips to show the English translation.

Click ❌ if you don’t know it (keeps the word).

Click ✅ if you know it (removes the word from the list).

Your progress is saved in data/words_to_learn.csv.
🌍 Future Improvements
Add support for more languages (Spanish, German, etc.)

Add scoring or tracking features

Add language selection dropdown

Dark mode or custom themes

📄 License
This project is open-source. Feel free to fork and build on it!

🙋‍♂️ Author
Made with 💙 by Arnold🙋‍♂️ Author



