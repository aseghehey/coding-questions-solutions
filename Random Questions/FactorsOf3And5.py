
# high, low
cnt = 0
low, high = 200, 405
for i in range(10):
    for j in range(10):
        if low <= (3**i * 5**j) <= high:
            cnt += 1

print(cnt)