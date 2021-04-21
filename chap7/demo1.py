# 时间：2021/4/11 10:50
items = [' Fruits', 'Books', 'Others']
prices = [96, 78, 85]
d = {item: price for item, price in zip(items, prices)}
print(d)
