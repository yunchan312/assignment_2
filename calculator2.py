# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

class Calculator:
    def __init__(self):
        self.Value = 0
        self.memory = 0

    def setValue(self, x):
        self.Value = x

    def getValue(self):
        return self.Value

    def add(self, x):
        self.Value += x

    def sub(self, x):
        self.Value -= x

    def mpy(self, x):
        self.Value *= x

    def div(self, x):
        self.Value //= x

    def mod(self, x):
        self.Value %= x

    def changeSign(self):
        self.Value = -self.Value

    def clear(self):
        self.Value = 0

    def memorySave(self):
        self.memory = self.Value

    def memoryRead(self):
        self.Value = self.memory
        return self.Value

    def memoryClear(self):
        self.Value = 0

    def memoryAdd(self):
        self.memory += self.Value

    def memorySub(self):
        self.memory -= self.Value



