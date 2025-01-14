#不区分大小写
s='Hello Python,Hello PhP,Hello Java'
word=input('请输入要统计的字符：')
word=word.upper()
new_s=s.upper()
print('{0}在{1}一共出现了{2}次'.format(word,s,new_s.count(word)))