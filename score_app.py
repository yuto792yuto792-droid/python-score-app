def calculate_stats(scores):
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)

    return average, highest, lowest

scores = []

with open("scores.csv", "r", encoding="utf-8") as file:
    for line in file:
        try:
            score = int(line.strip())

            if 0 <= score <= 100:
                scores.append(score)
            else:
                print(f"範囲外の点数をスキップしました: {score}")

        except ValueError:
            print(f"無効なデータをスキップしました: {line.strip()}")
        
if len(scores) == 0:
    print("点数が入力されていません")
    exit()

average, highest, lowest = calculate_stats(scores)

print(f"平均点は{average:.1f}点です")
print(f"最高点は{highest}点です")
print(f"最低点は{lowest}点です")

if average >= 60:
    result = "合格"
else:
    result = "不合格"

print(f"{result}です")

with open("result.csv", "w", encoding="utf-8") as file:
    file.write("平均点,最高点,最低点,判定\n")
    file.write(f"{average:.1f},{max(scores)},{min(scores)},{result}\n")