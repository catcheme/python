# 时间：2021/4/10 10:38
'''流程控制语句break与continue在二重循环中的使用'''
for i in range(5):  #代表外层循环要执行5次
    for j in range(1,11):
        if j%2==0:
            break
        print(j)

