"""
Encoding: UTF-8
Date: 2024/6/17
Name: 資工二Ａ吳承浚
twstock：獲取固定時段股票均量線
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
data_price = pd.DataFrame({'日期': date, '收盤價': price})

amount = stock.capacity
data_amount = pd.DataFrame({'日期': date, '成交量': amount})

# 计算5日、10日和20日均量线
five = date[4:]
average = stock.moving_average(amount, 5)
ma5 = pd.DataFrame({'日期': five, '5日平均成交量': average})

ten = date[9:]
average = stock.moving_average(amount, 10)
ma10 = pd.DataFrame({'日期': ten, '10日平均成交量': average})

twenty = date[19:]
average = stock.moving_average(amount, 20)
ma20 = pd.DataFrame({'日期': twenty, '20日平均成交量': average})

# 创建图表对象
result = pg.Figure()

# 添加收盘价折线
result.add_trace(
    pg.Scatter(
        x=data_price['日期'],
        y=data_price['收盤價'],
        name='收盤價'
    )
)

# 添加成交量折线，使用第二个y轴
result.add_trace(
    pg.Scatter(
        x=data_amount['日期'],
        y=data_amount['成交量'],
        yaxis='y2',
        name='成交量'
    )
)

# 添加5日均量线，使用第三个y轴
result.add_trace(
    pg.Scatter(
        x=ma5['日期'],
        y=ma5['5日平均成交量'],
        yaxis='y3',
        name='5日均量線'
    )
)

# 添加10日均量线，使用第四个y轴
result.add_trace(
    pg.Scatter(
        x=ma10['日期'],
        y=ma10['10日平均成交量'],
        yaxis='y4',
        name='10日均量線'
    )
)

# 添加20日均量线，使用第五个y轴
result.add_trace(
    pg.Scatter(
        x=ma20['日期'],
        y=ma20['20日平均成交量'],
        yaxis='y5',
        name='20日均量線'
    )
)

# 更新图表布局
result.update_layout(
    title={
        'text': f'{stock.sid}均量線',
        'font': {'color': 'black', 'size': 96},
        'x': 0.5,
        'y': 0.98
    },
    hovermode='x unified',
    xaxis=dict(domain=[0.27, 1]),
    yaxis=dict(title='收盤價'),
    yaxis2=dict(
        title='MA均量線',
        anchor='free',
        overlaying='y',
        position=0.1899
    ),
    yaxis3=dict(
        title='成交量',
        anchor='free',
        overlaying='y',
        position=0.098
    ),
    yaxis4=dict(
        overlaying='y',
        visible=False
    ),
    yaxis5=dict(
        overlaying='y',
        visible=False
    ),
)

# 显示图表
result.show()