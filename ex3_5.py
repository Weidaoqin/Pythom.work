for i in range(1,12):
    if i%5==1:
        print('\n'+'{0}-- -- -- --{0}-- -- -- --{0}'.format('+'),end='')
    else:
        for n in range(1): 
            print('\n'+'{0}           {0}           {0}'.format(' '),end='')
            print('\n'+'{0}           {0}           {0}'.format('|'),end='')
