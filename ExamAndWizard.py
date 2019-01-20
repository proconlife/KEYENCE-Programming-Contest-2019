import numpy as np

n=int(input())
a=np.array(list(map(int,input().split())))
b=np.array(list(map(int,input().split())))

c=[]
for i in range(n):
    c.append(a[i] - b[i])

c.sort(reverse=True)
d=np.array(c)
z=np.sum(d < 0)

x=np.sum(d[ d < 0])
y=np.sum(d[ d > 0])

if x == 0:
    print("0")
    exit()

if x + y < 0:
    print("-1")
    exit()    

for i,num in enumerate(c):
    x += num
    if x >= 0:
        print(z+i+1)
        exit()
