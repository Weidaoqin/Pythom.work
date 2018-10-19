#e2.1TempConvert.py
TempStr = input("请输入带符号的温度值：")
if TempStr[-1] in ['f','F']:
    C = int((eval(TempStr[0:-1]) - 32)/1.8)
    print("转换后的温度是{}C".format(C))
elif TempStr[-1] in ['c','C']:
    F = int(1.8*eval(TempStr[0:-1]) + 32)
    print("转换后的温度是{}F".format(F))
else:
    print("格式错误")
