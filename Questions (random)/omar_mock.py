arr = []

for i in range(2, 100):
    arr.append(i)
    for j in range(2, i):
        if i % j == 0:
            arr.remove(i)
            break

print(arr)
