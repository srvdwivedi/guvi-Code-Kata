size = int(input())
stri = input()
res = []

vol = ['a','e','i','o','u','A','E','I','O','U']
for i in stri:
    if i in vol:
        stri = stri.replace(i,"")
print(stri[::-1])

