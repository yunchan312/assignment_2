class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key         # 키 (key)
        self.value = value    # 값 (value)
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        self.num = 0
    def search1(self, key):
        node = self.root
        while node is not None:
            if key == node.key:
                return node.value
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None
    def maximum(self):
        node = self.root
        if node is None:
            return None
        while node.right != None:
            node = node.right
        return node.key
    def insert(self, key, value):
        self.num = self.num + 1
        self.root = self._insertSubtree(self.root, key, value)
    def _insertSubtree(self, node, key, value): # 원소(key, value)가 저장된 노드를 반환
        if node == None:
            return TreeNode(key, value)
        elif key < node.key:              # 왼쪽 부트리에 노드를 삽입
            node.left = self._insertSubtree(node.left, key, value)
        elif key > node.key:              # 오른쪽 부트리에 노드를 삽입
            node.right = self._insertSubtree(node.right, key, value)
        else:
            pass
        return node
    def _minNode(self, node):
        if node.left == None:
            return node
        else:
            return self._minNode(node.left)
    def delete(self, key):
        self.num = self.num - 1
        self.root = self.deleteNode(self.root, key)
    def _deleteNode(self, node, key):  # node가 루트인 이진탐색트리에서 key와 같은 키의 노드 삭제
        if node == None:
            return None
        if key < node.key:  # 삭제할 키의 노드가 node의 왼쪽 부트리인 경우
            node.left = self._deleteNode(node.left, key)
            return node
        elif key > node.key:  # 삭제할 키의 노드가 node의 오른쪽 부트리인 경우
            node.right = self._deleteNode(node.right, key)
            return node
        else:  # node가 삭제할 키의 노드인 경우
            if node.right == None:  # node의 오른쪽 자식노드가 없을 경우
                return node.left
            if node.left == None:  # node의 왼쪽 자식노드가 없을 경우
                return node.right

            rightMinNode = self._minNode(node.right)  # node의 오른쪽 부트리에서 최소키의 노드를 찾음
            node.key = rightMinNode.key  # node의 오른쪽 부트리에서 최소키의 노드를 복사 node에 복사
            node.value = rightMinNode.value
            node.right = self._deleteNode(node.right, node.key)  # node의 오른쪽 부트리에서 최소키의 노드를 삭제
            return node
    def numofStudents(self):
        print(self.num)
    def printEverything(self):
        node = self.root
        while node is not None:
            print(self.key)
            node = node.left


classStudents = BST()
while True:
    command = input()
    if command == 'N':
        classStudents.insert(input().split(), '')
    elif command == 'C':
        classStudents.delete(input().split())
    elif command == 'P':

    elif command == 'S':
        classStudents.numofStudents()
    elif command == 'Q':
        break