class Heap:
    def __init__(self):
        self.body = []

    def heap_push(self, obj):
        self.body.append(obj)
        i = len(self.body) - 1
        while i != 0:
            ip = (i - 1)//2
            if self.body[i] <= self.body[ip]:
                break
            else:
                self.body[i], self.body[ip], i = self.body[ip], self.body[i], ip

    def heap_pop(self):
        if len(self.body) == 1:
            return self.body.pop()
        result = self.body[0]
        self.body[0] = self.body.pop()
        i = 0
        while 2 * i + 2 < len(self.body) and self.body[i] < max(self.body[2 * i + 1], self.body[2 * i + 2]):
            if self.body[2 * i + 1] > self.body[2 * i + 2]:
                self.body[2 * i + 1], self.body[i] = self.body[i], self.body[2 * i + 1]
                i = 2 * i + 1
            else:
                self.body[2 * i + 2], self.body[i] = self.body[i], self.body[2 * i + 2]
                i = 2 * i + 2
        if 2 * i + 1 == len(self.body) - 1 and self.body[i] < self.body[2 * i + 1]:
            self.body[i], self.body[2 * i + 1] = self.body[2 * i + 1], self.body[i]
        return result

    def res(self):
        return self.body


def heap_sort(obj):
    heap_obj = Heap()
    for i in range(len(obj)):
        heap_obj.heap_push(obj[i])
    result = []
    for i in range(len(obj)):
        result.append(heap_obj.heap_pop())
    return result

A = [2, 5, 6, 6, 6, 7, 4, 2, 3, 4, 5, 6, 1, 5, 7]
A = heap_sort(A)
print(A)