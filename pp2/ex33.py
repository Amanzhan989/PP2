n = int(input())
print(str("{:.2f}".format(3.49*n))+"$","basic price")
print(str("{:.2f}".format(3.49*n*60/100))+"$","skidka")
print(str("{:.2f}".format(3.49*n*40/100))+"$","itogo")