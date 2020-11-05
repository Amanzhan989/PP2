a = list(map(int,input().split()))
maxi = 0
mini = 9999999999
for i in range(3):
    if a[i]<mini:
        mini = a[i]
    if a[i]>maxi:
        maxi = a[i]
print(mini,sum(a)-maxi-mini,maxi)

