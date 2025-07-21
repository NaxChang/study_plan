total = 0
count = 0
user_input = input("請輸入數字,直到輸入q結束: ")
while user_input != "q":
    num = float(user_input)
    total += num
    count += 1
    user_input = input("請輸入數字,直到輸入q結束: ")

if count == 0:
    result = 0
else:
    result = total / count

print(f"平均值:{result}")
print(f"總和為:{total}")
print(f"計數:{count}次")
