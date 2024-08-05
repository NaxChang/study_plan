import requests
import pandas as pd
import seaborn as sns

sns.set_theme(rc={'figure.dpi':300, 'font.sans-serif': 'Microsoft JhengHei'}, font_scale=0.8, palette='Set2')
url = 'https://www.taoyuan-airport.com/api/api/statistics/passenger/year'

payload = {"type":["入境","出境","過境"],
           "query":"new"}

resp = requests.post( url, data=payload )
df = pd.read_json( resp.text )
df.columns = ['年', '入境人數','出境人數','過境人數','totle']

df = df.drop('totle',axis=1)

df = df.set_index('年')
df['入境人數'] /= 10000   # df['入境人數'] = df['入境人數']/10000
df['出境人數'] /= 10000
df['過境人數'] /= 10000 
df.plot.bar(ylabel='人數(萬)', title='桃園機場近幾年出入境人數統計圖')

    