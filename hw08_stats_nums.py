def main():
    numbers = []
    file = open("numbers_file", "r")

    for line in file:
        line = line.strip()
        if line != "":
            number = float(line)
            numbers.append(number)

    if len(numbers) == 0:
        print("유효한 숫자가 없습니다.")
        return

    count = len(numbers)
    average = sum(numbers) / count
    max_value = max(numbers)
    min_value = min(numbers)

    numbers.sort()
    if count % 2 == 1:
        median = numbers[count // 2]
    else:
        median = (numbers[count // 2 - 1] + numbers[count // 2]) / 2

    print("총 숫자의 개수:", count)
    print("평균:", average)
    print("최댓값:", max_value)
    print("최솟값:", min_value)
    print("중앙값:", median)

if __name__ == "__main__":
    main()