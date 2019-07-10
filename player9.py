start,stop = map(int,input().split())
c = 0
for i in range(start,stop+1):
    f = 0
    for j in range(2,i):
        if i % j == 0:
            f = 1
            break
    if f == 0:
        c +=1
print(c)
        
