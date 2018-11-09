def isNum(n):
    try:
        n=eval(n)
        return True
    except:
        return False
while 1:
    print(isNum(input('请输入:')))
