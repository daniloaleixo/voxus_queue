# Filas

## Enunciado

Implemente uma classe de pilha de inteiros que possui os métodos push​, pop​ e min​, onde min​ retorna o menor inteiro na pilha e todos​ os métodos são executados em O(1)​.
Observação:​ Estas são as únicas restrições do problema. Não existe limite de memória nem nada do tipo.

## Como rodar o programa

Basta ter python instalado no computador e colocar na linha de comando
```bash
python filas.py
```


## Estratégia do algoritmo

O algoritmo para a implementação da fila usa como estratégia o fato de possuir duas filas: a fila que vamos guardar as informaçoes de fato e uma fila auxiliar que vamos usar para guardar os valores dos minimos.

A ideia é que nossa fila auxiliar vai manter sempre o minimo global acessivel alem de guardar outros minimos locais a medida que elementos são inseridos na fila principal.


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
As funções de pop(0) e append do python são implementados em tempo constante, assim podemos observar que no pior caso para uma chamada da função de push, como precisamos fazer o dequeue dos valores maiores que o novo valor a ser inserido, o algoritmo consome tempo O(m), onde m <= n e representa o tamanho da fila min_queue.

Porém se analisarmos duas operações em seguida é impossível que as duas sejam theta(m), pois cada um dos m elementos será inserido e removido apenas uma vez, o que nos leva a concluir que uma operação de push que remova m - k elementos, será seguida de uma interação que removerá no máximo k elementos, e portanto o algoritmo de push tem um custo amortizado de O(1).

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
