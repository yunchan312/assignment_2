
#find 약수
'''a = 0
def division(n):
    global a
    a += 1
    if n == a:
        return 1
    elif n%a==0:
        print(a, n)
        return division(n)+1
    else:
        return division(n)


e = division(12)
print(e)'''

'''
from StackClass import Stack

#infix to postfix(Stack)
def postToin(str):
    ops = Stack()
    nums = Stack()
    op = ['+', '-', '*', '/', '%']
    closebr = ')'
    openbr = '('
    for i in str:
        if i in op:
            ops.push(i)
        elif i == closebr:
            e = ops.pop()
            print(e, end='')
        else:
            if i != openbr:
                print(i, end='')


lst = input()
postToin(lst)
'''

