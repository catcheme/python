print('hello\nworld') #\转义字符的首字母     n-->newline的首字母表示换行
print('hello\tworld')
print('hello000\tworld')
print('hello\rworld') #world将hello覆盖
print('hello\bworld') #\b是退一个格

print('http:\\\\www.baidu.com')
print('老师说:\'大家好\'')

#原字符，不希望字符串的转义字符起作用，就使用原字符，就是在字符串之前加上r或者R
print(r'hello\nworld')
#注意最后一个字符不是能是反斜杠
#print(r'hellowolrd\')
print(r'hellowolrd\\')