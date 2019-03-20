def merges(x):
    if len(x) < 2:
        return x
    result = []
    mid = int(len(x) / 2)
    y = merges(x[:mid])
    z = merges(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result

x = [1,101,4,104,5,201,3,502,5,4]
print(merges(x))
