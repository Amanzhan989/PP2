b = float(input())
a = b*100
cnt = 0
while(a!=0):
    if(a>=200):
        a-=200
        cnt+=1
    if(a>=100 and a<200):
        a-=100
        cnt+=1
    if(a>=25 and a<100):
        a-=25
        cnt+=1
    if(a>=10 and a<25):
        a-=10
        cnt+=1
    if(a>=5 and a<10):
        a-=5
        cnt+=1
    if(a>=1 and a<5):
        a-=1
        cnt+=1
print(cnt)