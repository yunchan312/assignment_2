class Node:
    def __init__(self, e):
        self.data = e
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def clear(self):
        self.head = None
    def getNode(self, pos):
        if pos<0:
            return None
        node = self.head
        while pos > 0 and node != 0:
            node = node.link
            pos -= 1
        return node
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data
    def replace(self, pos ,e):
        node = self.getNode(pos)
        if node == None:
            print("Position Error")
        node.data = e
    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.link
        return count

    def insert(self, pos, e):
        node = Node(e)
        before = self.getNode(pos-1)
        if before == None:
            node.link = self.head
            self.head = node
        else:
            node.link = before.link
            before.link = node
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link
    def find(self, e):
        node = self.head
        count = 0
        while node.data != e:
            count += 1
            node = node.link
        return count
    def printList(self):
        lst = []
        node = self.head
        while node != None:
            lst.append(node.data)
            node = node.link
        return lst


s = LinkedList()
while True:
    list = input().split()
    if list[0] == 'N':
        s.insert(0, list[1])
    elif list[0] == 'C':
        pos = s.find(list[1])
        s.delete(pos)
    elif list[0] == 'S':
        studentcount = s.size()
        print(studentcount)
    elif list[0] == 'P':
        lst = s.printList()
        lst.sort()
        for i in lst:
            print(i, end=' ')
        print('')
    elif list[0] == 'Q':
        break;