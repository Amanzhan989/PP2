import math
t1,g1 = input().split()
t2,g2 = input().split()
t1 = int(t1) 
t1 = math.radians(t1)
g1 = int(g1)
t2 = int(t2)
t2 = math.radians(t2)
g2 = int(g2)
l = math.radians(g1-g2)
print(6371.01*(math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(l))))