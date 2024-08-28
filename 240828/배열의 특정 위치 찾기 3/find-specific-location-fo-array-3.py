array = list(map(int, input().split()))

add = 0
cnt = 0

while cnt < 100:
    if array[cnt] == 0:
        add += array[cnt-1]
        add += array[cnt-2]
        add += array[cnt-3]
        break
    cnt += 1

print(add)