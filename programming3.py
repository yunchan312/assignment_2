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
        except IndexError:
            print('Stack is empty')
    def size(self):
        return len(self.items)


def bracket_count(string):
    s = Stack()
    openParenthesis = '({['
    closeParenthesis = ')}]'

    for ch in string:
        if ch in openParenthesis:
            s.push(ch)
        elif ch in closeParenthesis:
            if s.isEmpty():
                return False
            else:
                openCh = s.pop()
                if (ch == ')' and openCh != '(') or (ch == '}' and openCh != '{') or (ch == ']' and openCh != '['):
                    return False
    return s.isEmpty()

str = input()

if bracket_count(str) == False:
    print('0')
else:
    print('1')