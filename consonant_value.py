def solve(word):
    vowels = "aeiou"
    consonant_values = [ord(char) - ord('a') + 1 for char in word if char not in vowels]
    return max(consonant_values, default=0)