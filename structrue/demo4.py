# 时间：2021/4/9 22:54
'''会员   >=200   8折
        >=100   9折
        |不打折
    非会员 >=200   9.5折
        |不打折'''
answer=input('您是会员吗？y/n')
money=float(input('请输入购物金额'))
#外层判断是否是会员
if answer=='y': #会员
    if money>=200:
        print('打8折，付款金额： ',money*0.8)
    elif money>=100:
        print('打9折，付款金额： ',money*0.9)
    else:
        print('不打折，付款金额： ',money)
else:
    if money>=200:
        print('打95折，付款金额： ',money*0.95)
    else:
        print('不打折，付款金额： ',money)

