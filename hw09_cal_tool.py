def total_calories(fruits, fruits_calorie_dic):
    total = 0
    for fruit in fruits:
        total += (fruits[fruit] / 100) * fruits_calorie_dic[fruit]
    return total

def read_db(filename):
    calorie_dic = {}
    with open(filename, encoding='utf-8-sig') as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            token = line.split(',')
            calorie_dic[token[0]] = int(token[1]) / int(token[2])
    return calorie_dic

def main():
    fruit_cal = read_db('./calorie_db.csv')
    fruit_eat = {'쑥': 200, '바나나': 200}
    total = total_calories(fruit_eat, fruit_cal)
    print(f"총 섭취 칼로리: {total:.2f} kcal")

if __name__ == "__main__":
    main()