import tkinter as tk
import random

class LottoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎲 로또 번호 생성기")
        self.root.geometry("400x300")

        self.label_title = tk.Label(root, text="로또 번호 생성기", font=("Arial", 20))
        self.label_title.pack(pady=20)

        self.label_numbers = tk.Label(root, text="번호를 생성하세요", font=("Arial", 16))
        self.label_numbers.pack(pady=20)

        self.button = tk.Button(root, text="번호 생성", font=("Arial", 16), command=self.generate_lotto)
        self.button.pack(pady=10)

    def generate_lotto(self):
        numbers = random.sample(range(1, 46), 6)
        numbers.sort()
        self.label_numbers.config(text="🎯 " + ", ".join(map(str, numbers)))

def main():
    root = tk.Tk()
    app = LottoGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()