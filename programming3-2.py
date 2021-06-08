class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def clear(self):
        self.items = []
    def push(self, e):
        self.items.append(e)
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return False

def evaluation(expr):
    s = Stack()
    op = ('+', '-', '*', '//', '%')
    for item in expr:
        if item in op:
            right_opr = s.pop()
            left_opr = s.pop()
            if (right_opr == False) or (left_opr == False):
                return False
            if item == '+':
                s.push(left_opr + right_opr)
            elif item == '-':
                s.push(left_opr - right_opr)
            elif item == '*':
                s.push(left_opr * right_opr)
            elif item == '//':
                s.push(left_opr // right_opr)
            elif item == '%':
                s.push(left_opr % right_opr)
        elif item == ';':
            break
        else:
            s.push(int(item))
    return s.pop()


token = ['+', '-', '*', '//', '%']
expr = input().split(token)
operator = []
print(expr)

if evaluation(expr) == False:
    print('error1')
else:
    print(evaluation(expr))