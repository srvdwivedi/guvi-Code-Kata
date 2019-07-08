nin=int(input())
l=list(map(int,input().split()))
vov=1
max=1
for i in range(1,nin):
    if(l[i]>l[i-1]):
        vov=vov+1
    else:
        if(max<vov):
            max=vov
        vov=1
if(max<vov):
    max=vov
print(max)
