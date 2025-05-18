def main():
    user_input = input("문자열을 입력하세요: ")
    toggled = toggle_text(user_input)
    print("변환 결과:", toggled)

def toggle_text(text: str) -> str:
    result = []

    for ch in text:
        ascii_code = ord(ch)

        if 'A' <= ch <= 'Z':  # 대문자 → 소문자
            result.append(chr(ascii_code + 32))
        elif 'a' <= ch <= 'z':  # 소문자 → 대문자
            result.append(chr(ascii_code - 32))
        else:  # 알파벳이 아닌 문자 그대로 유지
            result.append(ch)

    return ''.join(result)




if __name__ == "__main__":
    main()
