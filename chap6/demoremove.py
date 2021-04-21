# 时间：2021/4/10 20:48
lst=[10,20,30,40,50,60,30]
lst.remove(30)          #从列表中移除一个元素，若由此重复，则移除第一个重复元素
print(lst)
#lst.remove(100)        #ValueError: list.remove(x): x not in list
#pop()根据索引移除元素
lst.pop(1)
print(lst)
#lst.pop(5)             IndexError: pop index out of range    若指定的索引位置不存在，则抛出异常
lst.pop()               #若不指定参数，则默认删除最后一位
print(lst)


print('--------------切片操作，删除至少一个元素，将产生一个新的列表对象----------------')
new_list=lst[1:3]
print('原列表',lst,id(lst))
print('切片后的列表',new_list,id(new_list))

'''不产生新的列表对象，而是删除原列表中的内容'''
lst[1:3]=[]
print(lst)


'''清除列表中的所有元素'''
lst.clear()
print(lst)

'''del语句将列表对象删除'''
del lst
