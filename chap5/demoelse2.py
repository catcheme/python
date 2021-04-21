# 时间：2021/4/10 10:16
a=0
while a<3:
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码输入错误')
    #改变变量
    a+=1
else:
    print('对不起，三次密码输入错误')
