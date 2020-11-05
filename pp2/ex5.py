a = list(map(int,input().split()))
cnt = float(0)
for i in range(len(a)):
    if a[i]>1:
        cnt+=0.25
    else:
        cnt+=0.10
answer = "{:.2f}".format(cnt)
print(answer+"$")