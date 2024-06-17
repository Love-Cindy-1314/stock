"""
Encoding: UTF-8
Date: 2024/6/17
Name: 資工二Ａ吳承浚
twstock：獲取固定時間內股票均價線
"""
import twstock as t
import pandas as pd
import plotly.graph_objects as pg

info = input("請輸入股票代碼：")

# 获取股票数据
stock = t.Stock(info)
stock_name = stock.sid
date = stock.date
price = stock.price
data = pd.DataFrame({'日期': date, '收盤價': price})

# 计算5日、10日和20日均价线
five = date[4:]
average = stock.moving_average(price, 5)
ma5 = pd.DataFrame({'日期': five, '5日平均價格': average})

ten = date[9:]
average = stock.moving_average(price, 10)
ma10 = pd.DataFrame({'日期': ten, '10日平均價格': average})

twenty = date[19:]
average = stock.moving_average(price, 20)
ma20 = pd.DataFrame({'日期': twenty, '20日平均價格': average})

# 创建图表对象
result = pg.Figure()

# 添加收盘价折线
result.add_trace(
    pg.Scatter(
        x=data['日期'],
        y=data['收盤價'],
        name='收盤價'
    )
)

# 添加5日均价线
result.add_trace(
    pg.Scatter(
        x=ma5['日期'],
        y=ma5['5日平均價格'],
        name='5日均價線'
    )
)

# 添加10日均价线
result.add_trace(
    pg.Scatter(
        x=ma10['日期'],
        y=ma10['10日平均價格'],
        name='10日均價線'
    )
)

# 添加20日均价线
result.add_trace(
    pg.Scatter(
        x=ma20['日期'],
        y=ma20['20日平均價格'],
        name='20日均價線'
    )
)

# 显示图表
result.show()