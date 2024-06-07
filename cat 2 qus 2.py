def count_vowels_and_consonants(statement):
    vowels = "aeiouAEIOU"
    num_vowels = sum(1 for char in statement if char in vowels)
    num_consonants = sum(1 for char in statement if char.isalpha() and char not in vowels)
    return num_vowels, num_consonants

# Sample Input
statement = "Saveetha School of Engineering"

# Count vowels and consonants
num_vowels, num_consonants = count_vowels_and_consonants(statement)

# Determine which is maximum
max_count = "vowels" if num_vowels > num_consonants else "consonants" if num_consonants > num_vowels else "equal"

# Output the results
print(f"Number of vowels = {num_vowels}")
print(f"Number of consonants = {num_consonants}")
print(f"The number of {max_count} is maximum.")
