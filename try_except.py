try:
    n = 100 / int(input())
except ValueError:
    print("請輸入數字")
except ZeroDivisionError:
    print("請勿除以0")
# else:
#     print(n)
# finally:
#     # 無論是否發生例外都會執行
#     print("這是finally區塊")
print("OK")


# try:
#     n = 100 / int(input())
# except ValueError:
#     print("請輸入數字")
# except ZeroDivisionError:
#     print("請勿除以0")
# except Exception as e:
#     print("發生未知的錯誤", e, type(e))
# print("OK")
