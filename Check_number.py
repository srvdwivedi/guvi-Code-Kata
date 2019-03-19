def number(num):
    if num > 0:
        print("Positive")
    elif num == 0:
        print("Zero")
    else:
        print("Negative")
num = int(input())      
print(number(num))
