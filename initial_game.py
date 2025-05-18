import random

# 초성 리스트 (유니코드 순서대로)
CHOSUNG_LIST = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ',
    'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ',
    'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

def to_chosung_ch(ch):
    if '가' <= ch <= '힣':
        return CHOSUNG_LIST[(ord(ch) - ord('가')) // 588]
    else:
        return ch  

def to_chosung(text):
    return ''.join(to_chosung_ch(ch) for ch in text)

def main():
    problems = ["바나나", "딸기", "토마토", "복숭아"]
    solution = random.choice(problems)
    hint = to_chosung(solution)

    print("<<< 초성 퀴즈 >>>")
    is_correct = False
    for i in range(3):
        answer = input(f"문제 {i+1}/3: {hint} => ")
        if answer == solution:
            print("정답입니다!")
            is_correct = True
            break
        else:
            print("오답입니다.")
    
    if is_correct:
        print("잘하셨습니다.")
    else:
        print(f" 정답은 '{solution}'였습니다. 다시 도전해보세요!")

if __name__ == "__main__":
    main()
