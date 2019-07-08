nin=int(input())
l=list(map(int,input().split()))
lo1=l[1:nin:2]
lo2=l[0:nin:2]
if(sum(lo1)>=sum(lo2)):
    print(sum(lo1))
else:
    print(sum(lo2))
