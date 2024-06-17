import twstock
import pandas as pd
import plotly.express as px

# 輸入股票代碼
stock_code = input("請輸入股票代碼：")

# 使用 twstock 套件獲取股票歷史資料
stock = twstock.Stock(stock_code)
stock_name = stock.sid  # 股票代号
company_name = stock.name  # 公司名称
stock_data = stock.fetch_from(2021, 1)  # 從 2021 年 1 月開始獲取股票資料

# 將股票資料轉換為 pandas DataFrame
df = pd.DataFrame(stock_data)

# 使用 plotly 繪製股票圖表
fig = px.line(df, x='date', y=['close', 'open', 'high', 'low'], labels={'value': 'Price', 'date': 'Date'})

# 設定圖表標題
stock_name = stock.stocks[stock_code].name
fig.update_layout(title=f'{stock_code} - {stock_name}')

# 顯示圖表
fig.show()