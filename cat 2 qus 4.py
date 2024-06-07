def count_lines_and_words(paragraph):
    # Split the paragraph into lines
    lines = paragraph.split('\n')
    
    # Initialize the line counter
    num_lines = len(lines)
    
    # Print the number of lines
    print(f"Number of lines: {num_lines}")
    
    # Count and print the number of words in each line
    print("Number of words in each line:")
    for i, line in enumerate(lines):
        num_words = len(line.split())
        print(f"Line {i+1}: {num_words}")

# Sample Input
paragraph = '''This is the most straightforward way to count the number
of lines in a text file in Python. The readlines() method reads all
lines from a file and stores it in a list. Next, use the len() function
to find the length of the list which is nothing but total lines present in a file.'''

# Call the function with the sample input
count_lines_and_words(paragraph)
