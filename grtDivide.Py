num = int(input())
num2 = int(input())
list = []
rangee = max(num,num2)
for i in range(1,rangee):
    if (num%i==0) and (num2%i==0):
        list.append(i)
ss = sorted(list)
print(ss[-1])
