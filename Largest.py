def calculate_max(list1):
    maxelement = list1[0]
    for element in list1 :
        if element>maxelement:
            maxelement= element  
        return maxelement

l=input().split(" ")
result = calculate_max(l)
print(result)
