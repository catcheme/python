# 时间：2021/4/23 15:32
def fun(a, b, c):  # 函数声明是的参数，为形参
    print('a=', a)
    print('b=', b)
    print('c=', c)


fun(10, 20, 30)  # 函数调用时的参数传递，称为实参
lst = [11, 22, 33]
fun(*lst)  # 在函数调用时，将列表中的每个元素都转换为位置实参传入
print('------------------------')
fun(a=100, c=300, b=200)  # 函数的调用，所以是关键字实参
dic = {'a': 111, 'b': 222, 'c': 333}
fun(**dic)  # 在函数调用时，将字典中的键值对都转换为关键字实参输入
