x = "*"
y = " "
for l in range(3):
    print(" ")
for i in range(20):
    n = i
    if i > 5 :
        n = i - 3
    if i > 10 :
        n = i - 6
    if i > 15 :
        n = i - 9
    print(y*(20-n),end="")
    print(x*n,end="")
    print(x*(n-1))
for m in range(10):
    print(y*15,x*7)
for l in range(2):
    print(" ")