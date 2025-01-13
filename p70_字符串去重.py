#所谓字符串去重，只是将字符串中的各个字符唯一化，不是将字符串中的子字符串去重。
s='sdkfhiubqkerbib;dvba;sdbvlbfvlkbi3u2y834gtf233uyruohdvicabvkbiucgrqoi gefiihd vhiufhq iewhfewiuhdsnvkbfflklqdnflkasbfl;and'

#1 字符串拼接not in
new_s=''
for item in s: 
    print(item)
    if item not in new_s:
        new_s+=item
print(new_s)


print('\n'+'-'*50+'\n')

#2 用集合去重
new_s3=set(s)       #set函数：将字符串化为集合，（备注：集合不包含重复元素)，但元素的顺序是随机的
lst=list(new_s3)    #list函数：将字符串华为列表
print(lst)          
lst.sort(key=s.index)   #sort排序函数
print(''.join(lst))     #''.join：用空字符串拼接列表