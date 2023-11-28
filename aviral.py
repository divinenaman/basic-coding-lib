#
# # mod(a[i] - a[j]) <= limit
# assuming multiple swaps possible

# limit = 3
# 2 3 1 4

# random arr
a = [ 2, 3, 1, 4 ]

map = {}

# optimization
visited = {}

limit = 3

for i, val in enumerate(a):
    map[val] = i

for i, val in enumerate(a):
    # i - limit
    j = val - limit
    while j < val:
        if map.get(j) != None and map[j] > i:
            idx = map[j]
            a[idx], a[i] = a[i], a[idx]
            map[j] = i
            map[val] = idx
            break
        j = j + 1

    # i + limit
    j = val + limit
    while j > val:
        if map.get(j) != None and map[j] < i:
            idx = map[j]
            a[idx], a[i] = a[i], a[idx]
            map[j] = i
            map[val] = idx
            break
        j = j + 1


