def average(nums):
    avg=sum(nums)/len(nums)
    return avg
def main():
        num = average([1, 3, 5, 7, 9])
        print('평균은', num)

if __name__=='__main__':
    main()