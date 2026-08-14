score1 = int(input("1科目目の点数: "))
score2 = int(input("2科目目の点数: "))
score3 = int(input("3科目目の点数: "))

average = (score1 + score2 + score3) / 3

print(f"平均点は{average:.1f}点です")

if average >= 60:
    print("合格です")
else:
    print("不合格です")