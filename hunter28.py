word=input()
res=''.join(sorted(set(word),key=word.index))
print(res)
