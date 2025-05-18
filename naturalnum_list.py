def main():
    numbers = []

    while True:
        user_input = input("X=? ")

        if user_input == "-1":
            break

        
        if user_input.isdigit():
            number = int(user_input)
            if number >= 1:
                numbers.append(number)
        else:
            continue 

    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"\n입력된 값은 {numbers} 입니다. 총 {len(numbers)}개의 자연수가 입력되었고, 평균은 {average:.1f}입니다.")
    else:
        print("\n자연수가 입력되지 않았습니다.")

if __name__ == "__main__":
    main()
