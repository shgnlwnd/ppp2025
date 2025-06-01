import tkinter as tk
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("한글 행맨 게임")
        self.words = ["사과", "바나나", "복숭아", "포도", "레몬"]
        self.solution = random.choice(self.words)
        self.guessed_letters = set()
        self.trials = 6

        self.label_title = tk.Label(root, text="<<< 한글 단어 맞추기 >>>", font=("Arial", 18))
        self.label_title.pack(pady=10)

        self.label_word = tk.Label(root, text="", font=("Arial", 24))
        self.label_word.pack(pady=10)

        self.label_info = tk.Label(root, text=f"남은 기회: {self.trials}", font=("Arial", 14))
        self.label_info.pack()

        self.entry = tk.Entry(root, font=("Arial", 18), width=5, justify="center")
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="제출", command=self.check_letter, font=("Arial", 14))
        self.button.pack(pady=10)

        self.label_result = tk.Label(root, text="", font=("Arial", 14))
        self.label_result.pack()

        self.update_display()

    def update_display(self):
        current_state = " ".join([ch if ch in self.guessed_letters else "_" for ch in self.solution])
        self.label_word.config(text=current_state)
        self.label_info.config(text=f"남은 기회: {self.trials}")

        if "_" not in current_state:
            self.label_result.config(text="🎉 정답을 모두 맞췄습니다! 축하합니다.")
            self.disable_game()
        elif self.trials == 0:
            self.label_result.config(text=f"💥 게임 종료! 정답은 '{self.solution}'였습니다.")
            self.disable_game()

    def disable_game(self):
        self.entry.config(state="disabled")
        self.button.config(state="disabled")

    def check_letter(self):
        guess = self.entry.get().strip()
        self.entry.delete(0, tk.END)

        if len(guess) != 1:
            self.label_result.config(text="❗ 한 글자만 입력해주세요.")
            return

        if guess in self.guessed_letters:
            self.label_result.config(text="⚠️ 이미 입력한 글자입니다.")
            return

        self.guessed_letters.add(guess)

        if guess in self.solution:
            self.label_result.config(text=f"✅ '{guess}'는 단어에 포함되어 있습니다.")
        else:
            self.label_result.config(text=f"❌ '{guess}'는 단어에 없습니다.")
            self.trials -= 1

        self.update_display()

def main():
    root = tk.Tk()
    root.geometry("400x400")
    HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()