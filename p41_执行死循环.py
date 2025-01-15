#检察输出内容
for i in 'python':
    for j in range(2):
        print(i,end='')
        if i == 'h':
            break

print('\nj=',j,end='')


print('------------执行死循环------------')
i=0
while i<10:
    if i<1:
        print('i<1')
        continue
    else:
        print('i>1')
    i+=1
    