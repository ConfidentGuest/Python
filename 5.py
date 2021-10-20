n=int(input("Количество элементов: "))
a=[float(input())for i in range(n)]

s=0
p=1

for i in range(n):
    if a[i]>=0:
        s+=a[i]
    else:
        p*=a[i]

print(s, "Сумма")
print(p, "Произведение")