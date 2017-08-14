# Filas

## Enunciado

Implemente uma classe de pilha de inteiros que possui os métodos push​, pop​ e min​, onde min​ retorna o menor inteiro na pilha e todos​ os métodos são executados em O(1)​.
Observação:​ Estas são as únicas restrições do problema. Não existe limite de memória nem nada do tipo.

## Como rodar o programa

Basta ter python instalado no computador e colocar na linha de comando
```bash
python filas.py
```


## Análise do algoritmo

### Push
```python
def push(self, new_value):
	self.queue.enqueue(new_value)

	# dequeue all elements that are smaller than the new_value
	while not self.min_queue.is_empty() and self.min_queue.last() > new_value:
		self.min_queue.dequeue_back()
	self.min_queue.enqueue(new_value)

def enqueue(self, new_value):
	self.queue.append(new_value)

# Pop from the end of the queue
def dequeue_back(self):
	return self.queue.pop()
```
As funções de pop(0) e append do python são implementados em tempo constante, assim podemos observar que no pior caso temos uma função de push que roda em tempo O(n) já que precisamos fazer o dequeue dos valores maiores que o novo valor a ser inserido.

### Min

```python
def min(self):
	return self.min_queue.first()

def first(self):
	return self.queue[0]
```
Claramente a função min é O(1) já que ela faz um acesso direto ao primeiro elemento do array.


### Pop

```python
def pop(self):
	if not self.queue.is_empty():
		# remove from the min_queue if the element that i'm removing is the minimum 
		if self.min_queue.first() == self.queue.first():
			self.min_queue.dequeue()
		return self.queue.dequeue()

def dequeue(self):
    	return self.queue.pop(0)
```
Claramente a função pop também é O(1) já que os condicionais são verificados uma vez durante a chamada da função e chamam a função pop nativa do python que tem implementação em tempo constante.