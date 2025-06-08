import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import matplotlib


matplotlib.rcParams['font.family'] = 'AppleGothic'  


file_path = "champions_league_winners_korean.csv"  


df = pd.read_csv(file_path)


winner_counts = Counter(df["Winner"])

sorted_winners = sorted(winner_counts.items(), key=lambda x: x[1], reverse=True)
winners, counts = zip(*sorted_winners)


plt.figure(figsize=(12, 6))
plt.bar(winners, counts)
plt.title("챔피언스 리그 우승 횟수 (1956–2025)", fontsize=14)
plt.xlabel("클럽", fontsize=12)
plt.ylabel("우승 횟수", fontsize=12)
plt.xticks(rotation=75, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
