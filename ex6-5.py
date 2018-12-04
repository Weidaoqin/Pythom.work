from math import *
def shengri(n:int):
    birthday=[]
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range (n):
        year=[1999,2000]
        mouth=randint(1,12)
        if (years%400==0)and(years%4==0 and years%100!=0):
            day[1]=29
        else:
            day[1]=28
        day=randint(days[mouth-1])
        someday=(mouth,day)
        birthday.appen(someday)
    return birthdays
def shengri2(n:int):
    mun=0

    for i in range(n):
        people=shengri(23)
        pset=set(people)
        if len(pest)!=len(people):
            num+=1
    return num/n
def main():
    while True:
        n = int(input("输入一个重复的次数："))
        if n<0:
            break
        print("重复{}次，23个人中至少有两人生日相同的概率是：{}".format(n, shengri2(n)))
    

main()   

    
