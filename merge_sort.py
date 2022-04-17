def merge_sort(array):
    if len(array) == 1:
        return array
    left = merge_sort(array[0:len(array)//2])
    right = merge_sort(array[len(array)//2:len(array)])
    result = [0] * len(array)
    l_index, r_index, f_index = 0, 0, 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] <= right[r_index]:
            result[f_index] = left[l_index]
            l_index += 1
        else:
            result[f_index] = right[r_index]
            r_index += 1
        f_index += 1
    while l_index < len(left):
        result[f_index] = left[l_index]
        l_index += 1
        f_index += 1
    while r_index < len(right):
        result[f_index] = right[r_index]
        r_index += 1
        f_index += 1
    return result
