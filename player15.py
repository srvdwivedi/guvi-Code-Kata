ss=input()
ss=list(ss)
cc=[0]*256
for i in range(len(ss)):
    cc[ord(ss[i])]=ss.count(ss[i])
m=max(cc)
for i in range(256):
    if(m==cc[i]):
        print(chr(i))
