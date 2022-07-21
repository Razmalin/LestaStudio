# На языке Python (2.7) реализовать минимум по 2
# класса реализовывающих циклический буфер FIFO.
# Объяснить плюсы и минусы каждой реализации.

# Плюсы:
#
# 1. Операция доступа к самому старому элементу происходит за 0(1)
# 2. Добавление элемента происходит за 0(1)
# 3. Код легко понять
#
# Минусы:
#
# 1. Если нам нужен не самый старый элемент, то доступ к нему будет за 0(n)
# 2. Используется больше памяти

class MyCircularQueue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Добавляем элемент в круговую очередь
    def push(self, data):

        if (self.tail + 1) % self.k == self.head:
            self.pop()
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    # Удаляем элемент из очереди
    def pop(self):
        if self.head == -1:
            print("Круговая очередь пуста\n")

        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def printCQueue(self):
        if self.head == -1:
            print("В круговой очереди нет элементов")

        elif self.tail >= self.head:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


que = MyCircularQueue(5)
que.push(1)
que.push(2)
que.push(3)
que.push(4)
que.push(5)

print("Исходная очередь размером 5")
que.printCQueue()
que.push(6)
print("Очередь после добавления нового элемента")
que.printCQueue()
que.pop()
print("Из очереди удален элемент")
que.printCQueue()
