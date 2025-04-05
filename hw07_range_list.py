def get_range_list(n):
    numbers = list(range(1, n + 1))
    return (numbers)

def main():
    n = int(input("n값을 입력하세요: "))
    print(get_range_list(n))

if __name__ == '__main__':
    main()