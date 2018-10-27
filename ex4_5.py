import random
while True:
    try:
        k=random.randint(0,100)
        x=int(input("请输入一个0-100之间的整数:"))
        tem=0
        while x!=k:
          tem+=1
          if(x>k):
             print("遗憾，太大了")
          else:
             print("遗憾，太小了")
          x=int(input("请输一个入0-100之间的整数:"))
    except:
        print("输入内容必须为整数")
    else:
        print("预测{}次,你猜中了".format(tem))
        break
        

    

        
    
        
        

