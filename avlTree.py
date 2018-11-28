class Node():
	def __init__(self, value):
		self.value = value
		self.leftChild = None
		self.rightChild = None

	def __str__(self):
		return str(self.value)

class AVLTree():
	def __init__(self, data=None):
		self.node = None
		self.height = -1
		self.balance = 0

		if data is not None:
			for i in data:
				self.insert(i)

	def height_tree(self):
		if self.node:
			return self.node.height
		else:
			return 0

	def is_leaf(self):
		return self.height == 0

	def insert(self, value):
		tree = self.node
		newnode = Node(value)

		if tree == None:
			self.node = newnode
			self.node.leftChild = AVLTree()
			self.node.rightChild = AVLTree()
		elif value < tree.value:
			self.node.leftChild.insert(value)
		elif value > tree.value:
			self.node.rightChild.insert(value)

		#rebalanceando a árvore
		self.rebalance()

	def update_height(self, recursive=True):
		#atualizando a altura
		if self.node is not None:
			#recursive=true, percorre toda a árvore
			if recursive:
				if self.node.leftChild != None:
					self.node.leftChild.update_height()
				if self.node.rightChild != None:
					self.node.rightChild.update_height()

			#pegando a maior altura, entre as sub-árvores da esquerda e direita
			self.height = max(self.node.leftChild.height,
							  self.node.rightChild.height) + 1
		else:
			self.height = -1

	def update_balance(self, recursive=True):
		#atualizando o fator de balanceamento
		if not self.node == None:
			#recursive=true, percorre toda a árvore
			if recursive:
				if self.node.leftChild != None:
					self.node.leftChild.update_balance()
				if self.node.rightChild != None:
					self.node.rightChild.update_balance()
			
			#equação de balanceamento
			self.balance = self.node.leftChild.height - self.node.rightChild.height
		else:
			self.balance = 0

	def check_balanced(self):
		# fazendo o balancamento para ter certeza de que tudo está balanceado e atualizando a altura
		self.update_height()
		self.update_balance()
		if self == None or self.node == None:
			return True
		return (abs(self.balance) < 2) and self.node.leftChild.check_balanced() and self.node.rightChild.check_balanced()

	def rebalance(self):
		# atualizando a altura e o fator de balanceamento
		self.update_height(False)
		self.update_balance(False)
		while self.balance < -1 or self.balance > 1:
			if self.balance > 1:
				if self.node.leftChild.balance < 0:
					self.node.leftChild.lrotate()
					self.check_balanced()
				self.rrotate()
				self.check_balanced()

			if self.balance < -1:
				if self.node.rightChild.balance > 0:
					self.node.rightChild.rrotate()
					self.check_balanced()
				self.lrotate()
				self.check_balanced()

	def rrotate(self):
		#rodando para a direita, girando sobre si
		aux1 = self.node
		aux2 = self.node.leftChild.node
		T = aux2.rightChild.node

		self.node = aux2
		aux2.rightChild.node = aux1
		aux1.leftChild.node = T

	def lrotate(self):
		#rodando para a esquerda, girando sobre si
		aux1 = self.node
		aux2 = self.node.rightChild.node
		T = aux2.leftChild.node

		self.node = aux2
		aux2.leftChild.node = aux1
		aux1.rightChild.node = T

	def logical_successor(self, node):
		#achar o menor nó na sub-arvore da direita
		node = node.rightChild.node
		if node != None:
			while node.leftChild != None:
				if node.leftChild.node == None:
					return node
				else:
					node = node.leftChild.node
		return node

	def delete(self, value):
		if self.node != None:
			if self.node.value == value:
				#checando se o node atual é folha
				if self.node.leftChild.node == None and self.node.rightChild.node == None:
					self.node = None
				#checando se o filho esquerdo é nulo e atualizando o node
				elif self.node.leftChild.node == None:
					self.node = self.node.rightChild.node
				#checando se o filho direito é nulo e atualizando o node
				elif self.node.rightChild.node == None:
					self.node = self.node.leftChild.node

				#se os dois filhos existirem, deve-se encontrar um sucessor
				#para ficar no lugar do node excluido
				else:
					replacement = self.logical_successor(self.node)
					if replacement != None:
						self.node.value = replacement.value
						self.node.rightChild.delete(replacement.value)
				self.rebalance()
				return
			elif value < self.node.value:
				self.node.leftChild.delete(value)
			elif value > self.node.value:
				self.node.rightChild.delete(value)

			#rebalanceando a árvore
			self.rebalance()
		else:
			return

	def find(self, value):
		#encontrar o vule na sub-árvore e retornar seu node
		if self.node != None:
			if self.node.value == value:
				return self.node
			elif value < self.node.value:
				self.node.leftChild.find(value)
			elif value > self.node.value:
				self.node.rightChild.find(value)
		else:
			return

	def print_tree(self, level=0, pref="#"):
		#Atualizandoas heights antes de balancear
		self.update_height()
		self.update_balance()
		if (self.node != None):
			print('\t' * level * 2, pref, "[",self.node.value,"]", '$' if self.is_leaf() else ' ')
			if self.node.leftChild != None:
				self.node.rightChild.print_tree(level + 1, 'R')
			if self.node.leftChild != None:
				self.node.leftChild.print_tree(level + 1, 'L')