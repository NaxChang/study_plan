import os
import os.path
from datetime import datetime
import random

current_path = os.path.abspath(__name__)  # 取得當前腳本的絕對目錄
print(current_path)
directory_name = os.path.dirname(current_path)  # dirname , 找出原始路徑的父目錄
print(directory_name)
data_path = os.path.join(directory_name, "name")  # 表示當前目錄加上一個data目錄
print(data_path)
if not os.path.isdir(data_path):  # 檢查新目錄是否存在。
    print("沒有data的目錄,手動建立目錄")
    os.mkdir(data_path)
else:
    print("目錄已存在")

log_path = os.path.join(data_path, "iot.log")
if not os.path.isfile(log_path):
    with open(log_path, mode="w", encoding="utf8", newline="") as file:
        file.write("時間, 濕度, 溫度, 天氣\n")
else:
    print("有log檔")

now = datetime.now()
now_str = now.strftime("%Y-%m-%d %H:%M:%S")


humidity = str(random.randint(330, 820) / 10)
celsius = str(random.randint(50, 400) / 10)

log_path = os.path.join(data_path, "iot.log")
with open(log_path, mode="a", encoding="utf8", newline="") as file:
    file.write(now_str + "," + humidity + "," + celsius + "\n")
