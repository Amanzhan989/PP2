s = int(input())
d = int()
h = int()
m = int()
sec = int()
a = []
while(s>0):
    if(s>=86400):
        d+=1
        s-=86400
    if(s>=3600 and s<86400):
        h+=1
        s-=3600
    if(s>=60 and s<3600):
        m+=1
        s-=60
    if(s>=0 and s<60):
        sec+=s
        a.append(d)
        a.append(h)
        a.append(m)
        a.append(sec)        
        break
print(d,end=":")
for i in range(1,len(a)):
    if i==len(a)-1:
        if a[i]>=10:
            print(str(a[i]))
            exit()
        else:
            print("0"+str(a[i]))
            exit()
    if a[i]<10:
        print("0"+str(a[i]),end=":")
    else:
        print(str(a[i]),end=":")