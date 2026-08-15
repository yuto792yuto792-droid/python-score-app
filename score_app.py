score1 = int(input("1科目目の点数: "))
score2 = int(input("2科目目の点数: "))
score3 = int(input("3科目目の点数: "))

if 0 <= score1 <= 100 and 0 <= score2 <= 100 and 0 <= score3 <= 100:
    average = (score1 + score2 + score3) / 3

    print(f"平均点は{average:.1f}点です")

    if average >= 60:
        print("合格です")
    else:
        print("不合格です")
else:
    print("点数は0〜100の範囲で入力してください")