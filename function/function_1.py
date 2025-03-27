def greet(name="world"):
    print(f"Hello , {name}")


greet()
greet("Nameless")


# def shop(money):
#     if money <= 0:
#         return
#     print("購物中")


# shop(10)

# def add_and_subtract(a, b):
#     return a + b, a - b


# result = add_and_subtract(1, 2)
# print(result)  # 輸出：(3, -1)

# sum_result, diff_result = add_and_subtract(1, 2)


# # 拆解元組
# print(sum_result, diff_result)  # 輸出：3 -1

# add(1, 2)  # 合法
# add(b=2, a=1)  # 合法
# add(1, b=2)  # 合法
# # add(a=1, 2)      # 不合法，名稱參數不能在位置參數前
# # add(1, a=1)      # 不合法，名稱參數不能指定已經傳入的參數

# r1 = add(a=1, b=2)
# r2 = add(b=3, a=4)
# print(r1, r2)

# def greet(name):
#     print(f"Hello World {name}")


# greet("Tom")

# # print()
