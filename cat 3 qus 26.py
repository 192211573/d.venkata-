l = [2, 3, 4]
t = 6
left = 0
right = len(l) - 1
while left < right:
    c_sum = l[left] + l[right]
    if c_sum == t:
        print([left + 1, right + 1])
        break
    elif c_sum > t:
        right -= 1
    else:
        left += 1
else:
    result = []
    print(result)
