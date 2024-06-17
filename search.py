"""
Encoding: UTF-8
Date: 2024/6/17
Name: 資工二Ａ吳承浚
twstock：股票基本搜索
"""
import twstock as t
import pandas as pd
import plotly.express as pe

info = input("請輸入股票代碼：")

# 获取股票数据
stock = t.Stock(info)
stock_name = stock.sid
date = stock.date
price = stock.price
amount = stock.capacity

# 创建DataFrame并绘制收盘价折线图
data = pd.DataFrame({'日期': date, '收盤價': price})
result = pe.line(data, x='日期', y='收盤價', title=f'{stock.sid} 收盤價')
result.show()

# 创建DataFrame并绘制成交量柱状图
data = pd.DataFrame({'日期': date, '成交量': amount})
result = pe.bar(data, x='日期', y='成交量', title=f'{stock.sid} 成交量')
result.show()

data = pd.DataFrame({'日期':date,'成交量':price})
result = pe.bar(data, x='日期', y='成交量', title = f'{stock.sid}''成交量')
result.show()