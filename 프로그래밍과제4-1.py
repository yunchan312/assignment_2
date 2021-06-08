class Node:
    def __init__(self, element):
        self.link = None
        self.data = element
class LinkedStack:
    def __init__(self):
        self.top = None
    def isEmpty(self):
        return self.top == None
    def push(self, e):
        newNode = Node(e)
        newNode.link = self.top
        self.top = newNode
    def pop(self):
        if self.isEmpty():
            return
        e = self.top.data
        self.top = self.top.link
        return e

def bracketChecking(list):
    openbr = ['(', '{', '[']
    closebr = [')', '}', ']']
    s = LinkedStack()
    for i in list:
        if i in openbr:
            s.push(i)
        elif i in closebr:
            if i == ')':
                if s.pop() == '(':
                    result = 1
                else:
                    print('0')
                    return
            elif i == '}':
                if s.pop() == '{':
                    result = 1
                else:
                    print('0')
                    return
            elif i == ']':
                if s.pop() == '[':
                    result = 1
                else:
                    print('0')
                    return

    if s.isEmpty():
        print(result)
    else:
        print('0')
        return


e = list(input())
bracketChecking(e)




