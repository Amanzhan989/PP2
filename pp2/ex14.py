f = list(map(int,input().split()))
v = list(map(int,input().split()))
for i in range(len(f)):
    print("Your heigth is feet",f[i]*12*2.54,"cm")
for j in range(len(v)):
    print("Your heith is inches",v[j]*2.54,"cm")