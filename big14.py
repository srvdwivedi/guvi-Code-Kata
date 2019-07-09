start,stop = map(int,input().split())
for i in range(start+1,stop):
    if i %2==1:
        print(i,end=" ")
