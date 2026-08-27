scores = []

with open("scores.csv", "r", encoding="utf-8") as file:
    for line in file:
        try:
            score = int(line.strip())
            scores.append(score)
        except ValueError:
            print(f"無効なデータをスキップしました: {line.strip()}")
        
if len(scores) == 0:
    print("点数が入力されていません")
    exit()

average = sum(scores) / len(scores)

print(f"平均点は{average:.1f}点です")
print(f"最高点は{max(scores)}点です")
print(f"最低点は{min(scores)}点です")
if average >= 60:
    print("合格です")
else:
    print("不合格です")