class Queue:
    def __init__(self, e):
        self.MAX_QSIZE = e
        self.items = [0]*self.MAX_QSIZE
        self.front = -1
        self.rear = -1
        self.size = 0
    def isEmpty(self):
        return self.size == 0
    def enqueue(self, e):
        if self.size == len(self.items):
            print("Queue is full")
            self.resize(2*len(self.items))
        else:
            self.rear = (self.rear + 1)%(len(self.items))
            self.items[self.rear] = e
            self.size += 1
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            self.front = (self.front + 1)%(len(self.items))
            e = self.items[self.front]
            self.size -= 1
            return e

nwL = input().split()
n = int(nwL[0])
bridge_length = int(nwL[1])
weight = int(nwL[2])
truck_weights = input().split()
print(type(truck_weights[0]))

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0] * bridge_length

    while truck_weights:
        q.pop(0)
        if sum(q) + int(truck_weights[0]) <= weight:
            q.append(truck_weights.pop(0))
        else:
            q.append(0)
        answer += 1
    return answer + len(q)

print(solution(bridge_length, weight, truck_weights))

