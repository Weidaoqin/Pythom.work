#没有出现过终端的情况下
dayup, dayfactor,dayupa=1,0.01,1
for i in range(365):
    if i%11 in [3,4,5,6]:
        dayup=dayup*(1+dayfactor)
    else:
        dayup=dayup
print("十天休息一次:{:.2f}".format(dayup))
for  i in range(365):
    if i%16 in[4,5,6,7,11,12,13,14]:
        dayupa=dayupa*(1+dayfactor)
    else:
        dayupa=dayupa

print("十五天休息一次:{:.2f}".format(dayupa))
