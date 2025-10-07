import num2words as n2w

def number_letter_count(n):
    total_letters = 0
    for i in range(1, n + 1):
        word = n2w.num2words(i)
        word = word.replace(" ", "").replace("-", "")
        total_letters += len(word)
    return total_letters
print(number_letter_count(1000))

# Time Complexity: O(n * m)
# Space Complexity: O(1)