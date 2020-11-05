print("If you want enter  height in inches and weight in pounds select 1,\nIf you want enter height in metres and weith in kilogrammes select 2 ")
s = input()
w = int(input())
h = int(input())
if s=="1":
    print(w*703/(h*h))
else:
    print(w/(h*h))