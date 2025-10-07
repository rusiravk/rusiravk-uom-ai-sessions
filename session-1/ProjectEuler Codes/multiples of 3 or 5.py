n = 1000
multi3 = [x*3 for x in range(n) if x*3 <1000]
multi5 = [x*5 for x in range(n) if x*5 <1000]
multi = set(multi3 + multi5)
print(sum(multi))

# Time Complexity: O(n)
# Space Complexity: O(n)