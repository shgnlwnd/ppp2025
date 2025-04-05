def average(nums):
    avg = sum(nums) / len(nums)
    return avg

def main():
    numbers = input("숫자를 입력하세요")
    nums = numbers.split()
    nums = [int(x) for x in nums]
    num = average(nums)
    print('평균은', num)

if __name__ == '__main__':
    main()