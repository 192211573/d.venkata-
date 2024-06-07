def find_frequencies(arr):
    frequency_dict = {}
    for element in arr:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    return frequency_dict

# Example usage
array = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequencies = find_frequencies(array)
print(frequencies)
