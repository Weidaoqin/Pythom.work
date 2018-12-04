import jieba
txt=open("d:/红楼梦2.txt","r",encoding='GB18030').read()
words=jieba.lcut(txt)
excludes=[]
counts={}
for word in words:
    if len(word)==1 or len(word)==2:
        contine
    else:
        count[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
