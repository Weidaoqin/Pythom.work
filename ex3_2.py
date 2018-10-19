dayup, dayfactor,dayupa=1,0.01,1
for i in range(365):
    if i%7 in [3,4,5,6]:
        dayup=dayup*(1+dayfactor)
    else:
        dayup=dayup
print("连续努力365天:{:.2f}".format(dayup))
#print("10天休息一次:{:.}".format(dayup))
#print("15天休息一次:{:.}".format(dayppa))
