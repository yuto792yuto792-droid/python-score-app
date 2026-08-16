scores = []

while True:
    score = input("点数を入力してください（終了する場合は q）: ")

    if score == "q":
        break

    score = int(score)

    if 0 <= score <= 100:
        scores.append(score)
    else:
        print("点数は0〜100の範囲で入力してください")

average = sum(scores) / len(scores)

print(f"平均点は{average:.1f}点です")

if average >= 60:
    print("合格です")
else:
    print("不合格です")