"""
Encoding: UTF-8
Date: 2024/6/17
Name: 資工二Ａ吳承浚
twstock：獲取最佳4大買賣點
"""
import twstock as t

print("提示：\n根據輸入不同輸出的結果有差異。\nbuy&sell：若建議執行，則會輸出解釋原因；不行則為False但不會解釋理由。\nmix：True則為買，False則為賣，並會附上理由。")

info = input("請輸入股票代碼：")
test = input("请输入想要分析的買入賣出點(買入：buy，賣出：sell，綜合：mix)：")

stock = t.Stock(info)  # 创建股票对象
stock_name = stock.sid
b = t.BestFourPoint(stock)  # 创建BestFourPoint对象，用于分析股票
buy = b.best_four_point_to_buy()  # 获取买入建议
sell = b.best_four_point_to_sell()  # 获取卖出建议
mix = b.best_four_point()  # 获取综合建议

#根據輸入想要進行的操作做出相對應的分析
print("分析結果：")

if test == "buy":
    print(buy)
elif test == "sell":
    print(sell)
elif test == "mix":
    print(mix)
else:
    print("无效的输入")