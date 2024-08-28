arr = list(map(int, input().split()))

a = 0

for i in range(1, 11):
    if i % 2 == 0:
        a += arr[i-1]

m = 0
k = 0

for j in range(1, 11):
    if j % 3 == 0:
        m += arr[j-1]
        k += 1

m /= k
m = round(m , 1)

print(a, m)