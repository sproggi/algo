# 66397200

class Dequeue:
    def __init__(self, max_length):
        self.queue = [None] * max_length
        self.max_length = max_length
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_max_stack(self):
        return self.size == self.max_length

    def push_back(self, value):
        if self.is_max_stack():
            raise ValueError('error')
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_length
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise IndexError('error')
        value = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_length
        self.size -= 1
        return value

    def push_front(self, value):
        if self.is_max_stack():
            raise ValueError('error')
        self.queue[self.head - 1] = value
        self.head = (self.head - 1) % self.max_length
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError('error')
        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_length
        self.size -= 1
        return value


def main(commands_amount, size_queue):
    myqueue = Dequeue(size_queue)
    for _ in range(commands_amount):
        command = input().split()
        if command[0] == 'pop_front':
            if myqueue.is_empty():
                print('error')
            else:
                print(myqueue.pop_front())
        if command[0] == 'push_front':
            if myqueue.is_max_stack():
                print('error')
            else:
                myqueue.push_front(command[1])
        if command[0] == 'pop_back':
            if myqueue.is_empty():
                print('error')
            else:
                print(myqueue.pop_back())
        if command[0] == 'push_back':
            if myqueue.is_max_stack():
                print('error')
            else:
                myqueue.push_back(command[1])


if __name__ == '__main__':
    commands_amount, size_queue = int(input()), int(input())
    main(commands_amount, size_queue)
