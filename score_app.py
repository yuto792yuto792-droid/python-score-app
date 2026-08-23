scores = []

while True:
    score = input("点数を入力してください（終了する場合は q）: ")

    if score == "q":
        break

    try:
        score = int(score)
    except ValueError:
        print("数字を入力してください")
        continue

    if 0 <= score <= 100:
        scores.append(score)
    else:
        print("点数は0〜100の範囲で入力してください")

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