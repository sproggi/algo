def bubble_sort(input_list, num_amount):
    cnt = 0
    for i in range(0, num_amount - 1):
        flag = 0
        for j in range(0, num_amount - 1 - i):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
                flag = 1
                cnt += 1
        if flag == 0:
            break
        if flag == 1:
            print(*input_list, sep=' ')
    if cnt == 0:
        print(*input_list, sep=' ')


if __name__ == '__main__':
    amount = int(input())
    unsorted_list = [int(i) for i in input().split()]
    bubble_sort(unsorted_list, amount)
