#e2.2TempConvert.py
TempStr = input("请输入带符号的币种(人民币后面加y,美元加m)：")
if TempStr[-1] in ['m']:
    y = (eval(TempStr[0:-1]) * 6)
    print("转换后的人民币是{:.2f}m".format(y))
elif TempStr[-1] in ['y']:
    m = (eval(TempStr[0:-1]) / 6)
    print("转换后的美元是{:.2f}m".format(m))
else:
    print("格式错误")
