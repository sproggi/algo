def pasre_input(input_list):
    login, score, penalty = input_list
    return [-int(score), int(penalty), login]


def partition(array, start, end):
    pivot = (array[start])
    left = start + 1
    right = end - 1
    while left <= right:
        if array[left] < pivot:
            left += 1
        if array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
        else:
            array[start], array[right] = array[right], array[start]
    return right


def quicksort(array, start, end):
    if (end - start) > 1:
        delta = partition(array, start, end)
        quicksort(array, start, delta)
        quicksort(array, delta + 1, end)


if __name__ == '__main__':
    participants = int(input())
    input_list = [pasre_input(input().split()) for _ in range(participants)]
    quicksort(input_list, 0, participants)
    print(*(list(zip(*input_list))[2]), sep="\n")
