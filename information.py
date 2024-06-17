"""
Encoding: UTF-8
Date: 2024/6/17
Name: 資工二Ａ吳承浚
twstock：獲取股票基本資訊
"""
import twstock as t
import pandas as pd

info = input("請輸入股票代碼：")

# 获取股票实时数据
stock = t.realtime.get(info)
print(stock['success'])

# 创建DataFrame并提取所需数据
result = pd.DataFrame(stock).T.iloc[1:3]
result.columns = ['股票代碼','地區','股票名稱','公司全名','現在時間','最新成交價','成交量','累積成交量','最佳5檔賣出價','最佳5檔賣出量','最佳5檔買進價','最佳5檔買進價','開盤價','最高價','最低價']
print(result)