t = float(input())
v = float(input())
a = 13.12+0.6215*t-11.37*(v**0.16)+0.3965*t*(v**0.16)
if(a+0.5>=int(a)+1):
    print(int(a)+1)
else:
    print(int(a))