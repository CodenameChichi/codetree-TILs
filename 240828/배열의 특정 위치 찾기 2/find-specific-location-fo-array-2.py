arr = list(map(int, input().split()))

odd = 0
even = 0
cal = 0

for i in range(10):
    if (i+1) % 2 == 0:
        even += arr[i]
    else:
        odd += arr[i]

if odd < even:
    cal = even - odd
else:
    cal = odd - even

print(cal)