# 时间：2021/4/10 10:24
for item in range(1,10):
    for item1 in range(1,item+1):
        print(str(item1)+'*'+str(item)+'='+str(item1*item),end='\t')
    print()
