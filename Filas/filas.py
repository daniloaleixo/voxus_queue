#!/usr/bin/python
# -*- coding: utf-8 -*-

class Queue:
    def __init__(self):
        self.queue = []

    def get_queue(self):
    	return self.queue

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, new_value):
    	self.queue.insert(0, new_value)

    def dequeue(self):
    	return self.queue.pop()

# class QueueImplementation:
# 	def __init__(self):
# 		self.queue = Queue()
# 		self.min_queue = Queue()

# 	def push(self, new_value):
# 		self.queue.enqueue(new_value)

#     # def popi(self):
#     # 	return self.min_queue.dequeue()

# 	def printQueue(self):
# 		print '-> QUEUES:'
#     	print 'queue', self.queue
#     	print 'min_queue', self.min_queue

q = Queue()
q.enqueue(1)
print q.get_queue()
q.enqueue(2)
print q.get_queue()
q.enqueue(3)
print q.get_queue()
q.dequeue()
print q.get_queue()

