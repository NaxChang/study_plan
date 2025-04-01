"""
讓電腦隨機選擇一個介於 1 和 100 之間的數字（包含 1 和 100）。
接著，提示使用者猜測一個數字。系統會檢查使用者輸入的數字是否有效，並確認其在合法範圍內。

如果使用者猜的數字大於電腦選擇的數字，範圍會調整為 1 到使用者猜的數字減 1。
如果使用者猜的數字小於電腦的數字，範圍會調整為使用者猜的數字加 1 到 100。
這個過程會持續進行，直到使用者猜中正確的數字為止。
"""

import random

start = 1
end = 100
ans = random.randint(start, end)
guess_count = 0
print(ans)

while True:
    user_input = input(f"請輸入一個介於 {start } ~ {end} 之間的整數: ")

    try:
        user_input = int(user_input)

    except ValueError:
        print("請輸入一個整數: ")
        continue

    if not (start <= user_input <= end):
        print(f"請輸入介於{start}與{end}之間的數字")
        continue
    guess_count += 1
    if user_input == ans:
        print(f"恭喜答對,我輸入幾{guess_count}次!!")
        break

    if user_input < ans:
        start = user_input + 1
    else:
        end = user_input + 1
