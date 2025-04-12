def read_wt(filename):
    t_a = []
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()[1:]
        for line in lines:
            tokens = line.strip().split(",")
            try:
                tem = float(tokens[4])
                t_a.append(tem)
            except ValueError:
                continue  # 결측치가 있을 경우 넘어감
    return t_a

def read_water(filename):
    water = []
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()[1:]
        for line in lines:
            tokens = line.strip().split(",")
            try:
                w_all = float(tokens[9])
                if w_all >= 5:
                    water.append(w_all)
            except ValueError:
                continue
    return water

def read_allwater(filename):
    al_w = []
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()[1:]
        for line in lines:
            tokens = line.strip().split(",")
            try:
                w_lines = float(tokens[9])
                al_w.append(w_lines)
            except ValueError:
                continue
    return al_w

def main():
    # 👉 여기에 절대 경로 사용
    filename = "weather(146)_2022-2022.csv"
    year_average = read_wt(filename)
    up_5mm = read_water(filename)
    all_water = read_allwater(filename)

    if year_average:
        total_tem = sum(year_average)
        tem_len = len(year_average)
        print(f"연 평균 기온은 {(total_tem / tem_len):.2f}℃이다.")
    else:
        print("기온 데이터가 없습니다.")

    water_len = len(up_5mm)
    print(f"연 강수량이 5mm 이상인 날짜는 {water_len}일이다.")

    total_water = sum(all_water)
    print(f"연 강수량은 총 {total_water:.1f}mm입니다.")

if __name__ == "__main__":
    main()