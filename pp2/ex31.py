a = list(map(int,input().split()))
print(a[0],end="+")
for i in range(1,len(a)):
    if i==len(a)-1:
        print(str(a[-1])+"="+str(sum(a)))
    else:
        print(str(a[i]),end="+")