def read_data():
    data = []
    with open('./weather(146)_2001-2022.csv', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]: 
            parts = line.strip().split(',')
            day = {}
            day['year'] = int(parts[0])
            day['month'] = int(parts[1])
            day['day'] = int(parts[2])
            day['tmax'] = float(parts[3])
            day['tmin'] = float(parts[5])
            day['tavg'] = float(parts[4])
            data.append(day)
    return data

def max_diurnal(data):
    result = {}
    years = []
    for d in data:
        if d['year'] not in years:
            years.append(d['year'])
    years.sort()

    for y in years:
        max_gap = -1000
        max_day = None
        for d in data:
            if d['year'] == y:
                gap = d['tmax'] - d['tmin']
                if gap > max_gap:
                    max_gap = gap
                    max_day = d
        date = f"{max_day['year']}/{max_day['month']:02d}/{max_day['day']:02d}"
        result[y] = (date, max_gap)
    return result

def sum_temp(data):
    result = {}
    years = []
    for d in data:
        if d['year'] not in years:
            years.append(d['year'])
    years.sort()

    for y in years:
        total = 0
        for d in data:
            if d['year'] == y and 5 <= d['month'] <= 9:
                total += d['tavg']
        result[y] = total 
    return result

def main():
    data = read_data()

    diurnal = max_diurnal(data)
    tempsum = sum_temp(data)

    print("[1] 연도별 최대 일교차 발생 일자와 일교차")
    for y in sorted(diurnal.keys()):
        print(f"{diurnal[y][0]} {diurnal[y][1]:.1f}") 

    print("\n[2] 연도별 5~9월 적산온도")
    for y in sorted(tempsum.keys()):
        print(f"{y} {tempsum[y]:.1f}") 

if __name__ == "__main__":
    main()
