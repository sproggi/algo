num_dict = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


def check(result, n, start):
    if n == len(result[0]):
        return result
    empty_list = []
    for i in result:
        for j in work_list[start]:
            empty_list.append(i+j)
    result = empty_list
    return check(result, n, start+1)


if __name__ == '__main__':
    work_list = [num_dict[i] for i in input()]
    n = len(work_list)
    print(*check([''], n, 0), end=' ')
