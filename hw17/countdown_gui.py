import tkinter as tk
import time

class CountdownGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("카운트다운")
        self.seconds = 5

        self.label = tk.Label(root, text="", font=("Arial", 48))
        self.label.pack(pady=30)

        self.start_button = tk.Button(root, text="시작", command=self.start_countdown, font=("Arial", 16))
        self.start_button.pack()

    def start_countdown(self):
        self.start_button.config(state="disabled")
        self.countdown(self.seconds)

    def countdown(self, n):
        if n > 0:
            self.label.config(text=f"{n}...")
            self.root.after(1000, self.countdown, n - 1)
        else:
            self.label.config(text="💥 BOMB!!")

def main():
    root = tk.Tk()
    root.geometry("300x200")
    app = CountdownGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()