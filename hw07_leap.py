def is_leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                print(f"{y}년은 윤년입니다.")
            else:
                print(f"{y}년은 평년입니다.")
        else:
            print(f"{y}년은 윤년입니다.")
    else:
        print(f"{y}년은 평년입니다.")

def main():
    year = int(input("연도를 입력하세요: "))
    is_leap_year(year)

if __name__ == '__main__':
    main()