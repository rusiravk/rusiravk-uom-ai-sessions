def special_pythagorean_triplet(n):
    for a in range(1, n):
        for b in range(a, n - a):
            c = n - a - b
            if a * a + b * b == c * c:
                return a * b * c
    return None
result = special_pythagorean_triplet(1000)
print(result)

# Time Complexity: O(n^2)
# Space Complexity: O(1)
