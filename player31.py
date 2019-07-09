string= input()
open_ = 0
close = 0
for i in string:
    if i == '(':
        open_ += 1
    else:
        close +=1
if open_ == close:
    print("yes")
else:
    print("no")
