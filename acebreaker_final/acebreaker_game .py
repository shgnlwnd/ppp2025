import tkinter as tk
from PIL import Image, ImageTk
import random
import os
import pygame
    
START_CAPITAL = 50_000_000

class AceBreakerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("카드게임 시뮬레이션")
        self.root.geometry("1000x800")

        pygame.mixer.init()

        self.user_capital = START_CAPITAL
        self.ai_level = 0
        self.ai_capital = self.get_ai_capital()

        self.card_images = self.load_card_images()
        self.user_cards = []
        self.deck = []
        self.reroll_used = False
        self.round_results = {}

        self.setup_start_screen()

    def get_ai_capital(self):
        return [50_000_000, 80_000_000, 100_000_000][self.ai_level]

    def load_card_images(self):
        card_images = {}
        path_prefix = os.path.join(os.path.dirname(__file__), "images")
        cards = [str(i) for i in range(1, 10)] + ["Ace", "Joker"]
        for card in cards:
            path = os.path.join(path_prefix, f"card_{card.lower()}.png")
            img = Image.open(path).resize((100, 150))
            card_images[card] = ImageTk.PhotoImage(img)
        back_path = os.path.join(path_prefix, "card_back.png")
        back_img = Image.open(back_path).resize((100, 150))
        card_images['Back'] = ImageTk.PhotoImage(back_img)
        return card_images

    def setup_start_screen(self):
        self.canvas = tk.Canvas(self.root, width=1000, height=800)
        self.canvas.pack(fill="both", expand=True)

        try:
            bg_path = os.path.join(os.path.dirname(__file__), "images", "background.png")
            bg_image = Image.open(bg_path).resize((1000, 800))
            self.bg_img = ImageTk.PhotoImage(bg_image)
            self.canvas.create_image(0, 0, image=self.bg_img, anchor="nw")
        except Exception as e:
            print("배경 이미지 로드 실패:", e)

        self.start_button = tk.Button(self.root, text="시작", font=("Arial", 20), command=self.start_game)
        self.canvas.create_window(500, 400, window=self.start_button)

    def start_game(self):
        self.canvas.destroy()
        self.start_button.destroy()
        self.create_widgets()

    def create_widgets(self):
        self.info_label = tk.Label(self.root, text="Ace Breaker", font=("Arial", 20, "bold"))
        self.info_label.pack(pady=10)

        self.rule_frame = tk.Frame(self.root)
        self.rule_label = tk.Label(self.rule_frame, text="게임 룰 설명을 보시겠습니까?", font=("Arial", 12))
        self.rule_label.pack(side=tk.LEFT, padx=5)
        self.rule_yes = tk.Button(self.rule_frame, text="Yes", command=self.show_rules)
        self.rule_skip = tk.Button(self.rule_frame, text="Skip", command=self.enable_betting)
        self.rule_yes.pack(side=tk.LEFT, padx=5)
        self.rule_skip.pack(side=tk.LEFT, padx=5)
        self.rule_frame.pack(pady=5)

        self.bet_label = tk.Label(self.root, text="베팅 금액을 입력하세요 (*베팅금액은 소지액 내에서만 가능합니다)", font=("Arial", 12))
        self.capital_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.bet_entry = tk.Entry(self.root, font=("Arial", 14))
        self.bet_entry.bind("<KeyRelease>", self.format_bet_entry)
        self.play_button = tk.Button(self.root, text="게임 시작", command=self.play_round, font=("Arial", 14))

        self.user_preview_frame = tk.Frame(self.root)
        self.user_preview_labels = [tk.Label(self.user_preview_frame) for _ in range(3)]
        for lbl in self.user_preview_labels:
            lbl.pack(side=tk.LEFT, padx=5)
        self.user_preview_frame.pack(pady=5)
        self.user_preview_frame.pack_forget()

        self.user_card_title = tk.Label(self.root, text="", font=("Arial", 14))
        self.user_card_title.pack()
        self.user_card_frame = tk.Frame(self.root)
        self.user_card_labels = [tk.Label(self.user_card_frame)]
        self.user_card_labels[0].pack(side=tk.LEFT)
        self.user_card_frame.pack(pady=10)

        self.ai_card_title = tk.Label(self.root, text="", font=("Arial", 14))
        self.ai_card_title.pack()
        self.ai_card_frame = tk.Frame(self.root)
        self.ai_card_labels = [tk.Label(self.ai_card_frame)]
        self.ai_card_labels[0].pack(side=tk.LEFT)
        self.ai_card_frame.pack(pady=10)

        self.reroll_frame = tk.Frame(self.root)
        self.reroll_label = tk.Label(self.reroll_frame, text="카드를 다시 뽑으시겠습니까? (1회 한정)", font=("Arial", 12))
        self.reroll_label.pack(side=tk.LEFT, padx=5)
        self.yes_button = tk.Button(self.reroll_frame, text="Yes", command=self.reroll_yes)
        self.no_button = tk.Button(self.reroll_frame, text="No", command=self.reroll_no)
        self.yes_button.pack(side=tk.LEFT, padx=5)
        self.no_button.pack(side=tk.LEFT, padx=5)

        self.result_text = tk.Text(self.root, height=15, width=80, font=("Courier", 13))
        self.result_text.pack(pady=10)
        self.result_text.config(state=tk.DISABLED)

        self.next_button_frame = tk.Frame(self.root)
        self.next_game_button = tk.Button(self.next_button_frame, text="다음 라운드", command=lambda: self.enable_betting(from_restart=True))
        self.exit_button = tk.Button(self.next_button_frame, text="종료", command=self.root.destroy)
        self.next_button_frame.pack_forget()

    def format_bet_entry(self, event=None):
        current_text = self.bet_entry.get()
        cursor_pos = self.bet_entry.index(tk.INSERT)
        raw = ''.join(filter(str.isdigit, current_text))
        if raw:
            try:
                num = int(raw)
                formatted = f"{num:,}원"
                self.bet_entry.delete(0, tk.END)
                self.bet_entry.insert(0, formatted)
                diff = len(formatted) - len(current_text)
                self.bet_entry.icursor(cursor_pos + diff)
            except ValueError:
                pass
        else:
            self.bet_entry.delete(0, tk.END)

    def display_message(self, text, append=False):
        self.result_text.config(state=tk.NORMAL)
        if not append:
            self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, text + "\n")
        self.result_text.config(state=tk.DISABLED)
        self.root.update()

    def show_rules(self):
        rules = (
                "[에이스 브레이커 게임 룰]\n"
                "- 당신의 초기 자본은 5천만원입니다.\n"
                "- 당신의 자본이 0원이 되면 게임 오버입니다.\n"
                "- AI의 자본이 0원이 되면 승리입니다.\n"
                "- 총 3단계가 있으며, 각 단계 승리 시 다음 난이도로 넘어갑니다.\n"
                "- 3단계를 모두 클리어하면 게임 클리어입니다.\n"
                "- 각 플레이어는 카드 3장을 받습니다.\n"
                "- 한라운드에 1번 뽑은 카드를 다시 뽑을 수 있습니다. 이떄 3장을 전부 다시 뽑습니다.\n"
                "- 라운드는 총 3번 진행되며, 2승을 먼저 달성한 쪽이 라운드 승리입니다.\n"
                "- 1, 3라운드는 숫자가 큰 쪽이 승리,\n"
                "  2라운드는 숫자가 작은 쪽이 승리합니다.\n"
                "- Ace 카드는 모든 숫자를 이기며,\n"
                "- Joker 카드는 Ace를 이기며 숫자 카드에 집니다.\n"
                "- 행운을 빕니다.\n"
    )

    
    
        self.display_message(rules)
        self.next_button = tk.Button(self.root, text="다음", command=self._after_rule)
        self.next_button.pack(pady=10)

    def _after_rule(self):
        self.next_button.pack_forget()
        self.enable_betting()

    def enable_betting(self, from_restart=False):
        self.rule_frame.pack_forget()
        self.next_button_frame.pack_forget()
        if from_restart:
            self.info_label.pack_forget()
            self.user_card_labels[0].config(image="")
            self.ai_card_labels[0].config(image="")
            self.user_card_title.config(text="")
            self.ai_card_title.config(text="")
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state=tk.DISABLED)

        self.bet_label.pack(pady=2)
        self.capital_label.config(
            text=f"\U0001f4b0 현재 자본\n - 당신: {self.user_capital:,}원\n - AI: {self.ai_capital:,}원"
        )
        self.capital_label.pack(pady=2)
        self.bet_entry.delete(0, tk.END)
        self.bet_entry.pack(pady=5)
        self.play_button.pack(pady=12)

    def play_card_sound(self):
        try:
            pygame.mixer.music.load("sounds/card_swipe.mp3")
            pygame.mixer.music.play()
        except Exception as e:
            print("사운드 재생 실패:", e)

    def play_round(self):
        try:
            bet = int(self.bet_entry.get().replace(',', '').replace('원', ''))
        except ValueError:
            self.display_message("잘못된 베팅 금액입니다. 숫자만 입력해주세요.")
            return
        if bet <= 0 or bet > self.user_capital:
            self.display_message(f"베팅 금액은 당신의 자본 ({self.user_capital:,}원)을 초과할 수 없습니다.")
            return
        self.current_bet = bet
        self.deck = self.create_deck()
        used = set()
        self.user_cards = []
        while len(self.user_cards) < 3 and self.deck:
            card = self.draw_card(self.deck)
            if card not in used:
                self.user_cards.append(card)
                used.add(card)
        self.user_preview_frame.pack()
        for i, card in enumerate(self.user_cards):
            self.user_preview_labels[i].config(image=self.card_images[card])
        self.reroll_used = False
        self.reroll_frame.pack(pady=5)
        self.bet_label.pack_forget()
        self.capital_label.pack_forget()
        self.bet_entry.pack_forget()
        self.play_button.pack_forget()

    def reroll_yes(self):
        if not self.reroll_used:
            used = set()
            self.user_cards = []
            while len(self.user_cards) < 3 and self.deck:
                card = self.draw_card(self.deck)
                if card not in used:
                    self.user_cards.append(card)
                    used.add(card)
            for i, card in enumerate(self.user_cards):
                self.user_preview_labels[i].config(image=self.card_images[card])
            self.reroll_used = True
        self.reroll_frame.pack_forget()
        self.root.after(1000, lambda: self.resolve_round(self.current_bet))

    def reroll_no(self):
        self.reroll_frame.pack_forget()
        self.root.after(1000, lambda: self.resolve_round(self.current_bet))

    def resolve_round(self, bet):
        self.round_results = {'User': 0, 'AI': 0}
        self.ai_card_title.config(text="AI 카드")
        self.user_preview_frame.pack_forget()
        self.round_index = 0
        self.ai_cards = []
        ai_used = set(self.user_cards)
        while len(self.ai_cards) < 3 and self.deck:
            card = self.draw_card(self.deck)
            if card not in ai_used:
                self.ai_cards.append(card)
                ai_used.add(card)
        self._animate_round()

    def _animate_round(self):
        if self.round_index >= 3:
            self._end_round()
            return
        i = self.round_index
        user_card = self.user_cards[i]
        ai_card = self.ai_cards[i]
        round_num = i + 1
        self.display_message(f"{round_num}라운드 시작", append=(i > 0))
        self.user_card_labels[0].config(image=self.card_images['Back'])
        self.ai_card_labels[0].config(image=self.card_images['Back'])

        def show_user_card():
            self.user_card_labels[0].config(image=self.card_images[user_card])
            self.display_message(f"플레이어 카드: {user_card}", append=True)
            self.play_card_sound()

        def show_ai_card():
            self.ai_card_labels[0].config(image=self.card_images[ai_card])
            self.display_message(f"AI 카드: {ai_card}", append=True)
            self.play_card_sound()

        def resolve_match():
            result = self.compare_cards(user_card, ai_card, round_num)
            if result in self.round_results:
                self.round_results[result] += 1
            rule = "큰 숫자 승" if round_num in [1, 3] else "작은 숫자 승"
            winner = "무승부" if result == 'Draw' else ("플레이어 승" if result == 'User' else "AI 승")
            self.display_message(f"{round_num}라운드 ({rule}): 플레이어={user_card}, AI={ai_card} → {winner}", append=True)
            self.round_index += 1
            self.root.after(1000, self._animate_round)

        self.root.after(1000, show_user_card)
        self.root.after(2000, show_ai_card)
        self.root.after(3000, resolve_match)

    def _end_round(self):
        bet = self.current_bet
        if self.round_results['User'] >= 2:
            self.user_capital += bet
            self.ai_capital -= bet
            msg = "🎉 당신이 이겼습니다!"
        elif self.round_results['AI'] >= 2:
            self.user_capital -= bet
            self.ai_capital += bet
            msg = "🤖 AI가 이겼습니다."
        else:
            msg = "🤝 무승부입니다."
        msg += f"\n\n💰 현재 자본\n - 당신: {self.user_capital:,}원\n - AI: {self.ai_capital:,}원"
        self.display_message(msg, append=True)

        for widget in self.next_button_frame.winfo_children():
            widget.pack_forget()
        self.next_button_frame.pack(pady=10)

        if self.user_capital <= 0:
            self.display_message("당신의 자본이 모두 사라졌습니다... 💀 게임 오버입니다.", append=True)
            retry_button = tk.Button(self.next_button_frame, text="다시 시도", command=self.restart_game)
            retry_button.pack(side=tk.LEFT, padx=10)
            self.exit_button.pack(side=tk.LEFT, padx=10)
        elif self.ai_capital <= 0:
            if self.ai_level < 2:
                self.ai_level += 1
                self.display_message("AI의 자본이 0원이 되었습니다! 🎉 당신이 완전히 승리했습니다!", append=True)
                next_level_button = tk.Button(self.next_button_frame, text="다음 난이도", command=self.next_level_game)
                next_level_button.pack(side=tk.LEFT, padx=10)
                self.exit_button.pack(side=tk.LEFT, padx=10)
            else:
                self.display_message("🏆 모든 난이도를 클리어 했습니다! 축하합니다! 🎉", append=True)
                restart_button = tk.Button(self.next_button_frame, text="처음부터", command=self.restart_game)
                restart_button.pack(side=tk.LEFT, padx=10)
                self.exit_button.pack(side=tk.LEFT, padx=10)
        else:
            self.next_game_button.config(state=tk.NORMAL)
            self.next_game_button.pack(side=tk.LEFT, padx=10)
            self.exit_button.pack(side=tk.LEFT, padx=10)

    def next_level_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.user_capital = START_CAPITAL
        self.ai_capital = self.get_ai_capital()
        self.user_cards = []
        self.deck = []
        self.reroll_used = False
        self.round_results = {}
        self.create_widgets()
        self.enable_betting()

    def restart_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.user_capital = START_CAPITAL
        self.ai_level = 0
        self.ai_capital = self.get_ai_capital()
        self.user_cards = []
        self.deck = []
        self.reroll_used = False
        self.round_results = {}
        self.setup_start_screen()

    def create_deck(self):
        deck = [str(i) for i in range(1, 10)] * 4 + ['Ace', 'Joker']
        random.shuffle(deck)
        return deck

    def draw_card(self, deck):
        return deck.pop()

    def card_value(self, card):
        if card == 'Ace': return 100
        if card == 'Joker': return -1
        return int(card)

    def compare_cards(self, user_card, ai_card, round_num):
        # 조커는 에이스한테는 이기고 숫자 카드한테는 짐
        if user_card == 'Joker' and ai_card == 'Ace':
            return 'User'
        if ai_card == 'Joker' and user_card == 'Ace':
            return 'AI'
        if user_card == 'Joker' and ai_card not in ['Ace', 'Joker']:
            return 'AI'
        if ai_card == 'Joker' and user_card not in ['Ace', 'Joker']:
            return 'User'

        # 일반 비교
        user_val = self.card_value(user_card)
        ai_val = self.card_value(ai_card)
        if round_num in [1, 3]:
            return 'User' if user_val > ai_val else 'AI' if user_val < ai_val else 'Draw'
        else:
            return 'User' if user_val < ai_val else 'AI' if user_val > ai_val else 'Draw'
    
def main():
    root = tk.Tk()
    app = AceBreakerGame(root)
    root.mainloop()

if __name__ == '__main__':
    main()
