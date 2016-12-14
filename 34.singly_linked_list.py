class LinkedList:
    def __init__(self):
        self._begin = None

    def push_front(self, data):
        self._begin = [data, self._begin]

    def pop_front(self):
        if not self._begin:
            raise IndexError
        popped_obj = self._begin[0]
        self._begin = self._begin[1]
        return popped_obj

    def empty(self):
        return not self._begin


def correct_braces_expression(sequence):
    left, right = ['{', '('], ['}', ')']
    braces, stack = dict(zip(left, right)), LinkedList()
    for brace in sequence:
        if brace in left:
            stack.push_front(brace)
        elif brace in right and (stack.empty() or brace != braces[stack.pop_front()]):
            return False
    return stack.empty()

print(correct_braces_expression('({(())})'))
'''Все операции выполняются за O(1)'''
