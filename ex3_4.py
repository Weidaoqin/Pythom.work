import math
s=0
n=eval(input("输入:"))
a=n
for i in range(1,6):
    b=a%10
    c=a//10
    a=c
    s=s+b*pow(10,5-i)
if s==n:
    print("是回文")
else:
    print("不是回文")
