# http://www.python.com.tw
# httsp://www.python.com.tw

web_str = input("請輸入網址: ")
if web_str.startswith("http://") or web_str.startswith("https://"):
    print("輸入網址格式正確")
else:
    print("輸入網址格式錯誤")
