# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

class Calculator:
    def __init__(self):
        self.Value = 0

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

    def clear(self):
        self.Value = 0

