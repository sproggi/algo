def binary_search(arr, num, left, right):
    if right < left:
        return -1
    mid = (left + right) // 2
    if arr[mid] == num:
        return mid
    elif arr[left] <= arr[mid]:
        if arr[left] <= num <= arr[mid]:
            return binary_search(arr, num, left, mid)
        return binary_search(arr, num, mid + 1, right)
    else:
        if arr[mid] <= num <= arr[right]:
            return binary_search(arr, num, mid + 1, right)
        return binary_search(arr, num, left, mid)


def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    return binary_search(nums, target, left, right)
