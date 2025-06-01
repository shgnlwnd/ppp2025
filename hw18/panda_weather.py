import requests
import pandas as pd
import os

def download_weather(station_id, year, filename):
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)

def submit_to_api(answer):
    URL = "https://api.taegon.kr/answer"
    resp = requests.post(URL, data={"answer": answer})
    print("서버 응답:", resp.text)

def question1():
    fname = "weather_146_2012.csv"
    if not os.path.exists(fname):
        download_weather(146, 2012, fname)
    df = pd.read_csv(fname)
    total_rainfall = round(df['rainfall'].sum(), 1)
    print("Q1: 2012년 연강수량 =", total_rainfall)
    submit_to_api(total_rainfall)

def question2():
    fname = "weather_146_2024.csv"
    if not os.path.exists(fname):
        download_weather(146, 2024, fname)
    df = pd.read_csv(fname)
    max_temp = round(df['tmax'].max(), 1)
    print("Q2: 2024년 최대기온 =", max_temp)
    submit_to_api(max_temp)

def question3():
    fname = "weather_146_2020.csv"
    if not os.path.exists(fname):
        download_weather(146, 2020, fname)
    df = pd.read_csv(fname)
    df['tdiff'] = df['tmax'] - df['tmin']
    max_diff = round(df['tdiff'].max(), 1)
    print("Q3: 2020년 최대 일교차 =", max_diff)
    submit_to_api(max_diff)

def question4():
    fname1 = "weather_119_2019.csv"
    fname2 = "weather_146_2019.csv"
    if not os.path.exists(fname1):
        download_weather(119, 2019, fname1)
    if not os.path.exists(fname2):
        download_weather(146, 2019, fname2)

    df1 = pd.read_csv(fname1)
    df2 = pd.read_csv(fname2)
    rain_diff = round(abs(df1['rainfall'].sum() - df2['rainfall'].sum()), 1)
    print("Q4: 2019년 강수량 차이 =", rain_diff)
    submit_to_api(rain_diff)

def main():
    question1()
    question2()
    question3()
    question4()

if __name__ == "__main__":
    main()

