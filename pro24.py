nin=int(input())
no1=2**nin
l1=[]
for i in range(0,no1):
    l=bin(i)[2:].zfill(nin)
    if(len(l)<len(bin(2**nin-1)[2:])):
        l1.append([l.count("1"),l])
    else:
        l1.append([l.count("1"),l])
l1.sort()
for i in range(len(l1)):
    print(l1[i][1])
