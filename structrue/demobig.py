# 时间：2021/4/9 23:03
'''从键盘输入两个整数，比较两个整数的大小'''
num_a=int(input('请输入第一个整数：'))
num_b=int(input('请输入第二个整数：'))
'''if num_a>=num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)
'''
print('使用条件表达式进行比较')
#if条件判断结果为True，则执行前面的语句，结果为False则执行后面的语句
print(num_a,'大于等于',num_b if num_a>=num_b else (num_a,'小于',num_b))