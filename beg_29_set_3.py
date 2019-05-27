num = int(input())
if num < 60:
    print('0'+" "+str(num))
else:
    if num>=60:
        hours = num // 60
        minutes = num % 60
        print("{} {} ".format(hours, minutes),end="")
