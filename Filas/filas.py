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
    	self.queue.append(new_value)

    # Pop from the end of the queue
    def dequeue_back(self):
    	return self.queue.pop()

    def dequeue(self):
    	return self.queue.pop(0)

    def last(self):
    	return self.queue[len(self.queue) - 1]

    def first(self):
    	return self.queue[0]

class QueueImplementation:
	def __init__(self):
		self.queue = Queue()
		self.min_queue = Queue()

	def push(self, new_value):
		self.queue.enqueue(new_value)

		# dequeue all elements that are smaller than the new_value
		while not self.min_queue.is_empty() and self.min_queue.last() > new_value:
			self.min_queue.dequeue_back()
		self.min_queue.enqueue(new_value)

	def pop(self):
		if not self.queue.is_empty():
			# remove from the min_queue if the element that i'm removing is the minimum 
			if self.min_queue.first() == self.queue.first():
				self.min_queue.dequeue()
			return self.queue.dequeue()

	def min(self):
		return self.min_queue.first()

	def printQueues(self):
		print '--- Estado Atual das Filas:'
		print 'queue: ', self.queue.get_queue()
		print 'min_queue: ', self.min_queue.get_queue()



myQueue = QueueImplementation()

# main loop

while(True):
	print '\n-------------------\n'
	myQueue.printQueues()
	print '\n'
	print '1) Adicionar um elemento na fila'
	print '2) Retirar um elemento da fila'
	print '3) Pegar o mínimo da fila'
	print '0) Sair'
	print 'Digite o número do comando:'

	n = int(raw_input().strip())

	if(n == 0):
		break
	elif(n == 1):
		print 'Digite o numero que deseja adicionar à fila'
		x = int(raw_input().strip())
		myQueue.push(x)
	elif(n == 2):
		print 'Elemento: ', myQueue.pop(), ' retirado da fila'
	elif(n == 3):
		print 'Minimo da fila: ', myQueue.min()











