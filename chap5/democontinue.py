# 时间：2021/4/10 10:08
'''要求输出1-50之间所有5的倍数，5,10,15.。。
    5的倍数的共同点：和5的余数为0
    什么样的书不是5的倍数，与5的余数不为0的数'''
for item in range(1,51):
    if item%5==0:
        print(item)

print('--------------使用continue------------------')
for item in range(1,51):
    if(item%5!=0):
        continue
    print(item)
