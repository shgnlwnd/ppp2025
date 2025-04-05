def total_calorie(fruits, fruits_calorie_dic):
    total_kcal = 0
    for fruit in fruits:
        if fruit in fruits_calorie_dic:
            kcal = (fruits_calorie_dic[fruit] * fruits[fruit]) / 100
            total_kcal += kcal
    return total_kcal
def main():
    fruits = {"딸기": 300, "한라봉": 150}
    fruits_calorie_dic = {"한라봉": 50, "딸기": 34, "바나나": 77}
    result = total_calorie(fruits, fruits_calorie_dic)
    print(f"총 칼로리는 {result:.2f} kcal입니다.")
if __name__=='__main__':
    main()