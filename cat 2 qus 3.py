def count_matching_characters(s1, s2):
    return sum(1 for i in range(min(len(s1), len(s2))) if s1[i] == s2[i])

# Sample Input
s1 = "what"
s2 = "watch"

# Find the number of matches
num_matches = count_matching_characters(s1, s2)

# Output the result
print(f"Number of matches: {num_matches}")
