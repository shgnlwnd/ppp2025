import tkinter as tk
import random

def problem(dan, mul, user_input):
    try:
        ans = int(user_input)
        if ans == dan * mul:
            return True, '정답'
        else:
            return False, f'오답 (정답: {dan * mul})'
    except ValueError:
        return False, "숫자를 입력해야 합니다."

class GugudanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("구구단 게임")
        self.score = 0
        self.total_problem = 5
        self.current_count = 0
        self.dan = 0
        self.mul = 0

        self.label_question = tk.Label(root, text="", font=("Arial", 24))
        self.label_question.pack(pady=10)

        self.entry_answer = tk.Entry(root, font=("Arial", 18))
        self.entry_answer.pack()

        self.button_submit = tk.Button(root, text="제출", command=self.submit)
        self.button_submit.pack(pady=10)

        self.label_result = tk.Label(root, text="", font=("Arial", 14))
        self.label_result.pack()

        self.label_score = tk.Label(root, text="", font=("Arial", 16))
        self.label_score.pack(pady=10)

        self.next_problem()

    def next_problem(self):
        if self.current_count >= self.total_problem:
            percent = (self.score / self.total_problem) * 100
            self.label_question.config(text="게임 종료")
            self.label_score.config(text=f"총점: {self.score}점 ({percent:.0f}점)")
            self.entry_answer.config(state="disabled")
            self.button_submit.config(state="disabled")
            return

        self.dan = random.randint(2, 9)
        self.mul = random.randint(1, 9)
        self.label_question.config(text=f"{self.dan} * {self.mul} = ?")
        self.entry_answer.delete(0, tk.END)
        self.current_count += 1

    def submit(self):
        user_input = self.entry_answer.get().strip()
        correct, message = problem(self.dan, self.mul, user_input)
        if correct:
            self.score += 1
        self.label_result.config(text=message)
        self.root.after(1000, self.next_problem)

def main():
    root = tk.Tk()
    root.geometry("400x300")
    GugudanGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()