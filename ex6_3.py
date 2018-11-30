str=input("请输入要分析的字符串，回车表示结束：")
while str!='':
    counts={}
    for ch in str:
        counts[ch]=counts.get(ch,0)+1
    items=list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)
    for i in range(len(items)):
        word,count=items[i]
        print("{0:<10}{1:>5}".format(word,count))
    str=input("请输入要分析的字符串，回车表示结束：")    
