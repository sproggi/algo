# 66533534

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError('error')
        return self.items.pop()


def operation(value, first_digit, second_digit):
    operations_dict = {
        '*': (lambda first_num, second_num: first_num * second_num),
        '/': (lambda first_num, second_num: first_num // second_num),
        '+': (lambda first_num, second_num: first_num + second_num),
        '-': (lambda first_num, second_num: first_num - second_num),
    }
    return operations_dict[value](first_digit, second_digit)


def main(input_string):
    stack = Stack()
    value_list = input_string.split(' ')
    for value in value_list:
        if value not in ['*', '/', '+', '-']:
            stack.push(int(value))
        else:
            second_num = stack.pop()
            first_num = stack.pop()
            result = operation(value, first_num, second_num)
            stack.push(result)
    return stack.items[-1]


if __name__ == '__main__':
    input_string = input()
    solution = main(input_string)
    print(solution)
