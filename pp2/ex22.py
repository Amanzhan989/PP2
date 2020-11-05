import math
s1,s2,s3 = input().split()
s1 = int(s1)
s2 = int(s2)
s3 = int(s3)
p = float((s1+s2+s3)/2)
print(math.sqrt(p*(p-s1)*(p-s2)*(p-s3)))