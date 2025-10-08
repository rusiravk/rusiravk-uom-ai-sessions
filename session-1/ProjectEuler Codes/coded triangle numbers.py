def isTriangleNumber(n):
    x = (8*n + 1)**0.5
    return x.is_integer() and (x - 1) % 2 == 0

def isCodedTriangleNumber(word):
    total = sum(POS[ch] for ch in word)
    return isTriangleNumber(total)

with open('words.txt', 'r') as file:
    content = file.read()
    words = content.replace('"', '').split(',')
    POS = {ch: i+1 for i, ch in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    count = sum(1 for word in words if isCodedTriangleNumber(word))
    print(count)

# Time Complexity: O(n * m)
# Space Complexity: O(1)