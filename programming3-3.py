# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

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
        except:
            print('error')
    def size(self):
        return len(self.items)

def evalPostfix(expr):
    s = Stack()
    token = ['+', '-', '*', '/', '//', '%']
    for item in expr:
        if item in token:
            val2 = s.pop()
            val1 = s.pop()
            if item == '+':
                s.push(val2+val1)
            elif item == '-':
                s.push(val2-val1)
            elif item == '*':
                s.push(val2*val1)
            elif item == '/':
                s.push(val2/val1)
            elif item == '//':
                s.push(val2//val1)
            elif item == '%':
                s.push(val2%val1)
        elif item == ';':
            break
        else:
            float(item)
            s.push(int(item))
    return s.pop()

expr = input().split()
try:
    result = evalPostfix(expr)
    print(result)
except:
    print('')