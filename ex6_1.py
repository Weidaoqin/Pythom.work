import random
strs=[]
for i in (65,97):
    for j in range(26):
        strs+=chr(i+j)
for i in range(10):
    strs+=str(i)
for i in range (10):
    print("密码",i+1,".",end='')
    for j in range(8):
          print(strs[random.randint(0,61)],end=' ')
    print()
                
