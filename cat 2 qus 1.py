# Take input from the user
string = input("Please enter a string: ")

# Initialize counters and lists
alphabets, num, special, space = 0, 0, 0, 0
a, d, spl = [], [], []

# Iterate through each character in the string
for char in string:
    if char.isalpha():
        alphabets += 1
        a.append(char)
    elif char.isdigit():
        num += 1
        d.append(char)
    elif char.isspace():
        space += 1
    else:
        special += 1
        spl.append(char)

# Print the results
print(f"Alphabet letters: {alphabets}, {a}")
print(f"Numbers: {num}, {d}")
print(f"Spaces: {space}")
print(f"Special characters: {special}, {spl}")
