def binary_search(arr, x, left, right):
    if left >= right:
        return left + 1
    if x > arr[right]:
        return -1
    mid = (left + right) // 2
    if arr[mid] < x:
        return binary_search(arr, x, mid + 1, right)
    if arr[mid] >= x:
        return binary_search(arr, x, left, mid)


if __name__ == "__main__":
    n_days = int(input())
    arr = [int(i) for i in input().split(' ')]
    x = int(input())
    index_1 = binary_search(arr, x, left=0, right=n_days-1)
    index_2 = binary_search(arr, x*2, left=0, right=n_days-1)
    print(index_1, index_2)
