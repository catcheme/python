# 时间：2021/4/9 22:42
'''多分支结构，多选一执行
    从键盘录入一个整数成绩
    90-100  A
    80-90   B
    70-80   C
    60-70   D
    0-60    E
    小于0或者大于100为非法数据（不在成绩的有效范围）'''
score=int(input('请输入一个成绩：'))
#判断
if score>=90 and score<=100:        #也可以写作if 90<=score<=100
    print('A级')
elif score>=80 and score<=89:
    print('B级')
elif score>=70 and score<=79:
    print('C级')
elif score>=60 and score<=69:
    print('D级')
elif score>=0 and score<=59:
    print('E级')
else:
    print('输入不合法')
