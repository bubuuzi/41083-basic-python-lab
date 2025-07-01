score_1 = int(input("Enter your score1: "))
score_2 = int(input("Enter your score2: "))
score_3 = int(input("Enter your score3: "))

total = score_1 + score_2 + score_3


if total == 100:
    print("คะแนนรวมสมบูรณ์ 100 คะแนน")

if total >= 80:
    print("A")
elif total >= 75:
    print("B+")
elif total >= 70:
    print("B")
elif total >= 65:
    print("C+")
elif total >= 60:
    print("C")
elif total >= 55:
    print("D+")
elif total >= 50:
    print("D")
else:
    print("F")
