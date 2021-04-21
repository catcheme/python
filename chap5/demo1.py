# 时间：2021/4/9 23:20
#range()的三种创建方式
'''第一种创建方式，只有一个参数（小括号中只给了一个数）'''
#range(stop)
r=range(10)     #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]，默认从0开始，默认相差1，称为步长
print(r)        #range(0,10)
print(list(r))  #用于查看range对象中的整数序列 -->list是列表的意思

'''第二种创建方式，给了两个参数（小括号中给了两个数）'''
#range(start,stop)
r=range(1,10)   #指定了起始值，从1开始，到10结束（不包含10），默认步长1
print(list(r))  #[1, 2, 3, 4, 5, 6, 7, 8, 9]

'''第三种创建方式，给了三个参数（小括号中给了三个数）'''
#ragne(start,stop,step)
r=range(1,10,2)
print(list(r))  #[1, 3, 5, 7, 9]


'''判断指定的整数 在序列中是否存在 in ，not in'''
print(10 in r)  #False,10不在当前的r的序列中
print(9 in r)   #Ture，9在序列中

print(10 not in r)
print(9 not in r)


#range类型的优点：不管range对象表示的整数序列有多长，所有range对象占用的内存空间都是相同的，
#因为仅仅需要存储start，stop和step，只有当用到range对象时，才会去计算序列中的相关元素