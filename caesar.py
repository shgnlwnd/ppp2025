def main():
    text = input("암호화할 문장을 입력하세요: ")
    shift = 3 
    
    encoded = caesar_encode(text, shift)
    print(f"암호화된 결과: {encoded}")
    
    decoded = caesar_decode(encoded, shift)
    print(f"복호화된 결과: {decoded}")




def caesar_encode(text: str, shift: int = 3) -> str:
    result = []
    for char in text:
        if char.isupper():
            
            shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
            result += chr(shifted)
        elif char.islower():
        
            shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
            result += chr(shifted)
        else:
            result += char  # 공백, 숫자, 기호 등은 그대로
    return result

def caesar_decode(text: str, shift: int = 3) -> str:
    result = []
    for char in text:
        if char.isupper():
            shifted = (ord(char) - ord('A') - shift) % 26 + ord('A')
            result += chr(shifted)
        elif char.islower():
            shifted = (ord(char) - ord('a') - shift) % 26 + ord('a')
            result += chr(shifted)
        else:
            result += char
    return result



if __name__ == "__main__":
    main()
