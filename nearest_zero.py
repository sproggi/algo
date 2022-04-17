def nearest_zero(houses_numbers, street_length):
    cnt = houses_numbers.index(0)
    for i in range(street_length):
        if houses_numbers[i] == 0:
            cnt = 0
            houses_numbers[i] = cnt
        else:
            cnt += 1
            houses_numbers[i] = cnt
    for i in range(1, street_length + 1):
        if houses_numbers[-i] == 0:
            cnt = 0
            houses_numbers[-i] = cnt
        else:
            cnt += 1
            houses_numbers[-i] = min(houses_numbers[-i], cnt)
    return houses_numbers


if __name__ == "__main__":
    street_length = int(input())
    houses_numbers = list(map(int, input().rstrip().split()))
    result_list = nearest_zero(houses_numbers, street_length)
    print(*result_list, sep=' ')
