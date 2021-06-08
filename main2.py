# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

from calculator2 import Calculator
cal = Calculator()

while True:
    command = input().split()
    if command[0] == 'setValue':
        cal.setValue(int(command[1]))
    elif command[0] == 'add':
        cal.add(int(command[1]))
    elif command[0] == 'sub':
        cal.sub(int(command[1]))
    elif command[0] == 'mpy':
        cal.mpy(int(command[1]))
    elif command[0] == 'div':
        cal.div(int(command[1]))
    elif command[0] == 'mod':
        cal.mod(int(command[1]))
    elif command[0] == 'clear':
        cal.clear()
    elif command[0] == 'currentValue':
        print(cal.getValue())
    elif command[0] == 'MS':
        cal.memorySave()
    elif command[0] == 'MR':
        cal.memoryRead()
    elif command[0] == 'M+':
        cal.memoryAdd()
    elif command[0] == 'M-':
        cal.memorySub()
    elif command[0] == 'MC':
        cal.memoryClear()
    elif command[0] == 'exit':
        exit()
