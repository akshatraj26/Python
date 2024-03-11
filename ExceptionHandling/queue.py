'''
Write a program that implements a queue data structure of specified size. If the queue becomes full
and we try to add an element to it, then a user-defined QueueError exception should be raised.
Similarly, if the queue is empty and we try to delete an element from it then a QueueError should be raised.
'''


class QueueError(Exception):
    def __init__(self, msg, front, rear):
        self.errmsg = msg + ' front = ' + str(front) + ' rear= ' + str(rear)

    def get_message(self):
        return self.errmsg


class Queue:

    def __init__(self, sz):
        self.size = sz
        self.queue = []
        self.front = self.rear = -1

    def enqueue(self, item):
        if self.rear == self.size - 1:
            raise QueueError("Queue is full.", self.front, self.rear)
        else:
            self.rear += 1
            self.queue += [item]

            if self.front == -1:
                self.front = 0

    def dequeue(self):
        if self.front == -1:
            raise QueueError("Queue is Empty.", self.front, self.rear)
        else:
            data = self.queue[self.front]
            # self.queue[self.front] = None
            # self.queue.pop(self.front)
            if self.front == self.rear:
                self.front = self.rear = -1

            else:
                self.front += 1
            return data

    def printall(self):
        print(self.queue)

# My example


if __name__ == '__main__':
    q = Queue(5)
    try:

        q.enqueue(45)
        q.enqueue(67)
        q.enqueue(78)
        q.enqueue(243)
        q.enqueue(23)
        q.printall()
        i = q.dequeue()
        print("Item deleted :- ", i)
        q.printall()
        i = q.dequeue()
        print("Item Deleted :- ", i)
        q.printall()
        i = q.dequeue()
        print("Item deleted :- ", i)
        q.printall()
        i = q.dequeue()
        print("Item Deleted :- ", i)
        # q.enqueue(12)
        # We can see that before executing the next I got the Queue Error
        q.printall()
        i = q.dequeue()
        print("Item Deleted :- ", i)
        i = q.dequeue()
        print("Item Deleted :- ", i)
    except QueueError as e:
        print(e.get_message())

# Book Examples
#
# q = Queue(5)
# try:
#     q.enqueue(11)
#     q.enqueue(12)
#     q.enqueue(13)
#     q.enqueue(14) # queue is full
#     # q.enqueue(15) # queue is full
#     q.printall()
#     i = q.dequeue()
#     print("Item Deleted =", i)
#     i = q.dequeue()
#     print("Item Deleted =", i)
#     i = q.dequeue()
#     print("Item Deleted =", i)
#     i = q.dequeue()
#     print("Item Deleted =", i)
#     i = q.dequeue()
#     print("Item Deleted =", i)
#     i = q.dequeue()  # oops queue is empty
#     print("Item Deleted =", i)
#

# except QueueError as e:
#     print(e.get_message())
#


