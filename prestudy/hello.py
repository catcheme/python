print('hello world')

#注意：1、所指定的盘符要存在；2、使用file=fp
fp=open('E:/text.txt','a+')
print('hello world',file=fp)
fp.close()

#不进行换行输出
print('hello','world','Python')