score = []
total = incore = 0
while incore != -1:
    incore = int(input("請輸入分數: "))
    score.append(incore)
print(f"共有幾位學生: {len(score) -1}")

for i in range(0, len(score) - 1):
    total += score[i]
    avg = total / (len(score) - 1)
print(f"總成績為: {total:.2f},平均成績為: {avg:.2f}")
