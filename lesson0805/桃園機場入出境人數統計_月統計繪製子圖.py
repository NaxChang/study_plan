import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://www.taoyuan-airport.com/api/api/statistics/passenger/month'

plt.figure( figsize=(10,20), dpi=300)
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'

payload = {"type":["入境","出境","過境"],
           "query":"new",
           "date":"2009-01-01",
           "endDate":"2023-05-31"}

resp = requests.post( url ,data=payload)
df = pd.read_json( resp.text )

df['年'] = df['mm09_yyymm']//100
df['月'] = df['mm09_yyymm']%100
df.columns = ['年月', '入境', '去年入境','出境',
              '去年出境', '過境', '去年過境', '總人數',
              '去年總人數', '年', '月']
colSort = ['年月', '年', '月','入境', '去年入境',
           '出境', '去年出境', '過境', '去年過境', 
           '總人數', '去年總人數']
df = df[ colSort ]

fig, ax = plt.subplots(2,2,figsize=(12,10),dpi=300)
df_2023 = df[ df['年']==2023 ]
# df_2023 = df_2023.iloc[:, [1,2,3,5,7]]
df_2023 = df_2023[ ['月','入境', '出境', '過境'] ]
df_2023 = df_2023.set_index('月')
df_2023.plot( kind='bar', ax=ax[0, 0])

df_2023 = df[ df['年']==2023 ]
df_2023 = df_2023.iloc[:, [1,2,3,5,7]]
df_2023long = pd.melt( df_2023, id_vars=['年','月'], var_name='型態', value_name='人數')
sns.barplot(data=df_2023long, x='月',y='人數', hue='型態', palette='Set2', ax=ax[0, 1])

df_arr = df.iloc[:, [1,2,3]]
sns.lineplot(data=df_arr, x='年', y='入境', ax=ax[1, 0], hue='月')

sns.lineplot(data=df_arr, x='月', y='入境', hue='年', ax=ax[1, 1])
plt.savefig('chart.png')

