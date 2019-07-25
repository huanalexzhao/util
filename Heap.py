#!/usr/bin/env python3
class Heap:
    def __init__(self, tag):
        self.heap = []
        self.length = 0
        self.tag = tag
    def insert(self,x):
        if self.length == len(self.heap):
            self.heap.append(x)
        else:
            self.heap[self.length] = x
        self.length += 1
        temp = self.length - 1
        while temp > 0:
            parent = (temp - 1) // 2
            if self.tag == 'min':
                if self.heap[temp] < self.heap[parent]:
                    self.heap[temp], self.heap[parent] = self.heap[parent], self.heap[temp]
                    temp = parent
                else:
                    break
            elif self.tag =='max':
                if self.heap[temp] > self.heap[parent]:
                    self.heap[temp], self.heap[parent] = self.heap[parent], self.heap[temp]
                    temp = parent
                else:
                    break
    def extract(self):
        if self.length == 0:
            return None
        self.heap[0], self.heap[self.length - 1] = self.heap[self.length - 1], self.heap[0]
        self.length -= 1
        temp = 0
        while True:
            left_child = temp * 2 + 1
            right_child = temp * 2 + 2
            if self.tag == 'min':
                if left_child >= self.length:
                    break
                if right_child >= self.length:
                    if self.heap[left_child] < self.heap[temp]:
                        self.heap[left_child], self.heap[temp] = self.heap[temps], self.heap[left_child]
                        temp = left_child
                    break

                if self.heap[left_child] <= self.heap[right_child]:
                    child = left_child
                else:
                    child = right_child
                if self.heap[temp] > self.heap[child]:
                    self.heap[temp], self.heap[child] = self.heap[child], self.heap[temp]
                    temp = child
                else:
                    break
            elif self.tag == 'max':
                if left_child <= self.length:
                    break
                if right_child <= self.length:
                    if self.heap[left_child] > self.heap[temp]:
                        self.heap[left_child], self.heap[temp] = self.heap[temps], self.heap[left_child]
                        temp = left_child
                        break

                if self.heap[left_child] >= self.heap[right_child]:
                    child = left_child
                else:
                    child = right_child
                if self.heap[temp] < self.heap[child]:
                    self.heap[temp], self.heap[child] = self.heap[child], self.heap[temp]
                    temp = child
                else:
                    break
        return self.heap[self.length]
    @property
    def priority(self):
        return self.heap[0]

class Median:
    def __init__(self):
        self.low_H = Heap('max')
        self.high_H = Heap('min')

    def add(self, x):
        if self.low_H.length == 0:
            self.low_H.insert(x)
            return
        if self.high_H.length == 0:
            if x > self.low_H.priority:
                self.high_H.insert(x)
            else:
                self.low_H.insert(x)
                temp = self.low_H.extract()
                self.high_H.insert(temp)
            return

        if x <= self.high_H.priority:
            self.low_H.insert(x)
        else:
            self.high_H.insert(x)
        if self.low_H.length >= self.high_H.length + 2:
            temp = self.low_H.extract()
            self.high_H.insert(temp)

        if self.low_H.length + 2 <= self.high_H.length:
            temp = self.high_H.extract()
            self.low_H.insert(temp)

    @property
    def median(self):
        if self.low_H.length == 0:
            return None
        if self.low_H.length > self.high_H.length:
            return self.low_H.priority
        elif self.low_H.length == self.high_H.length:
            return (self.low_H.priority + self.high_H.priority) / 2
        else:
            return self.high_H.priority

if __name__ == '__main__':
    m = Median()

    while True:
        x = input("Input a number, N to exit: ")
        if x == 'N':
            break
        else:
            m.add(int(x))
    print("The median of your inputs is: ", m.median)
