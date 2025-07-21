import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns

sns.set_theme(
    rc={"figure.dpi": 300, "font.sans-serif": "Microsoft JhengHei"},
    font_scale=0.8,
    palette="Set2",
)
url = "https://www.taoyuan-airport.com/api/api/statistics/passenger/year"

payload = {"type": ["入境", "出境", "過境"], "query": "new"}

resp = requests.post(url, data=payload)
df = pd.read_json(resp.text)
df.columns = ["年", "入境人數", "出境人數", "過境人數", "totle"]

df = df.drop("totle", axis=1)

df_long = df.melt(id_vars="年", var_name="方法", value_name="人數")
df_long["人數(萬)"] = df_long["人數"] / 10000
sns.barplot(data=df_long, x="年", y="人數(萬)", hue="方法")
# 使用 Seaborn 繪製條形圖
sns_plot = sns.barplot(data=df_long, x="年", y="人數(萬)", hue="方法")

# 設定圖片標題等其他設定（可選）
sns_plot.set_title("桃園機場旅客數據")
sns_plot.figure.savefig("airport_passenger_statistics.png")

# 顯示圖片（可選）
plt.show()
