n=int(input("Количество элементов: "))
a=[int(input())for i in range(n)]

s=0
p=1
g=0

for i in range(n):
    if (a[i-1]<=+5) and (a[i-1]>=-2):
        s+=a[i-1]
        p*=a[i-1]
        g+=1

print(s, "Сумма")
print(p, "Произведение")
print(g, "Количество")