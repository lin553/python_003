#s[start:end:step],      即s[开始:结束:步长]
s='hello world'

#正向序列
for i in range(0,len(s)):
    print(s[i],end='\t')

print('\n')

#反向序列
for i in range(1,len(s)+1):
    print(s[-i],end='\t')


print(end='\n')
print('---------------------------------')

#用s[start:end:step]格式输出，可少略某些参数
print(s[6::1])
print(s[0:5:])



print(end='\n')
print('---------------------------------')

print(s[-1::])
print(s[len(s)-1])



print(end='\n')
print('---------------------------------')

print(s[0::])
print(s[len(s)::])
#逆序输出
print(s[len(s)::-1])