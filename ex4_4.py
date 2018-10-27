import random
k=random.randint(0,100)
x=eval(input("请输入0-100之间的整数:"))
tem=0
while x!=k:
    tem+=1
    if(x>k):
        print("遗憾，太大了")
    else:
        print("遗憾，太小了")
    x=eval(input("请输入0-100之间的整数:"))
print("预测{}次,你猜中了".format(tem))
        
