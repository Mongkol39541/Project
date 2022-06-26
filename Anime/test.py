List1 = []
List2 = []
List3 = []
SDd = []
z = 0
m = 0
n = int(input("n : "))
k = 0
for i in range(n):
    x = float(input("x"+str(i)+": "))
    y = float(input("y"+str(i)+": "))
    z = x*y
    List1.append(z)
    List2.append(x)
    List3.append(y)
    k += y

Av = sum(List1)/k
print("Av = ",Av)

for j in range(n):
    m = (List2[j]-Av)**2
    Sd = m*(List3[j]/k)
    SDd.append(Sd)
Ans = sum(SDd)

print("Sd = ",Ans**(1/2))
print("Sd^2 = ",Ans)