def find_mth_max_nth_min(arr, M, N):
    # Remove duplicates and sort the array
    sorted_arr = sorted(set(arr))
    
    if M <= 0 or M > len(sorted_arr):
        return f"M = {M} is out of range. Valid range: 1 to {len(sorted_arr)}"
    if N <= 0 or N > len(sorted_arr):
        return f"N = {N} is out of range. Valid range: 1 to {len(sorted_arr)}"
    
    mth_max = sorted_arr[-M]
    nth_min = sorted_arr[N-1]
    
    sum_val = mth_max + nth_min
    difference = mth_max - nth_min
    product = mth_max * nth_min
    
    return f"{M}th Maximum Number = {mth_max}, {N}th Minimum Number = {nth_min}\n" \
           f"Sum = {sum_val}\nDifference = {difference}\nProduct = {product}"

# Sample Input
arr = [14, 16, 87, 36, 25, 89, 34]
M = 1
N = 3
print(find_mth_max_nth_min(arr, M, N))

# Test cases
test_cases = [
    ([16, 16, 16, 16, 16], 0, 1),
    ([0, 0, 0, 0], 1, 2),
    ([-12, -78, -35, -42, -85], 3, 3),
    ([15, 19, 34, 56, 12], 6, 3),
    ([85, 45, 65, 75, 95], 5, 7),
]

for i, (arr, M, N) in enumerate(test_cases, 1):
    print(f"\nTest Case {i}:")
    print(f"Array = {arr}, M = {M}, N = {N}")
    print(find_mth_max_nth_min(arr, M, N))
