nT = 285
while True:
    nT += 1
    T = nT * (nT + 1) // 2
    nP = (1 + (1 + 24 * T) ** 0.5) / 6
    nH = (1 + (1 + 8 * T) ** 0.5) / 4
    if nP == int(nP) and nH == int(nH):
        print(T)
        break

# Time Complexity: O(n)
# Space Complexity: O(1)