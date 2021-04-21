# 时间：2021/4/9 22:25
money=1000      #余额
s=int(input('请输入取款金额'))
#判断余额是否充足
if money>=s:                #单分支结构
    money=money-s
    print('取款成功，余额为：',money)