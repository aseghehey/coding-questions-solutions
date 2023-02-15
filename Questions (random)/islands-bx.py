import random

def find_largest_cluster(r, c, ROWS, COLS, m):
    if r < 0 or c < 0 or r >= ROWS or c >= COLS or m[r][c] == 0:
        return 0

    m[r][c] = 0 # mark visited
    return 1 + find_largest_cluster(r + 1, c, ROWS, COLS, m) + find_largest_cluster(r - 1, c, ROWS, COLS, m) + find_largest_cluster(r, c + 1, ROWS, COLS, m) + find_largest_cluster(r, c - 1, ROWS, COLS, m)
    
if __name__ == "__main__":
    m = []

    for i in range(4):
        tmp = []
        for j in range(4):
            tmp.append(random.choice([0,1]))
        m.append(tmp)

    print(m)
    ROWS = len(m)
    COLS = len(m[0])

    max_sum = 0
    for r in range(ROWS):
        for c in range(COLS):
            max_sum = max(max_sum, find_largest_cluster(r, c, ROWS, COLS, m))

    print(max_sum)

