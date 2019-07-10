s = input()
vol = ['a','e','i','o','u','A','E','I','O','U']
res = []
for i in s:
    if i not in vol:
        res.append(i)
r=res[::-1]
for i in r:
    print(i,end="")
