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

	def height(self):
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

		self.rebalance()

	def update_heights(self, recurse=True):
		if not self.node == None:
			if recurse:
				if self.node.leftChild != None:
					self.node.leftChild.update_heights()
				if self.node.rightChild != None:
					self.node.rightChild.update_heights()

			self.height = max(self.node.leftChild.height,
							  self.node.rightChild.height) + 1
		else:
			self.height = -1

	def update_balances(self, recurse=True):
		#atualizando o fator de balanceamento
		if not self.node == None:
			if recurse:
				if self.node.leftChild != None:
					self.node.leftChild.update_balances()
				if self.node.rightChild != None:
					self.node.rightChild.update_balances()
			#equação de balanceamento
			self.balance = self.node.leftChild.height - self.node.rightChild.height
		else:
			self.balance = 0

	def check_balanced(self):
		# fazendo o balancamento para ter certeza de que tudo está balanceado
		self.update_heights()
		self.update_balances()
		if self == None or self.node == None:
			return True
		return (abs(self.balance) < 2) and self.node.leftChild.check_balanced() and self.node.rightChild.check_balanced()

	def rebalance(self):
		self.update_heights(False)
		self.update_balances(False)
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
		A = self.node
		B = self.node.leftChild.node
		T = B.rightChild.node

		self.node = B
		B.rightChild.node = A
		A.leftChild.node = T

	def lrotate(self):
		#rodando para a esquerda, girando sobre si
		A = self.node
		B = self.node.rightChild.node
		T = B.leftChild.node

		self.node = B
		B.leftChild.node = A
		A.rightChild.node = T

	def logical_successor(self, node):
		#achar o menor value na sub-arvore da direita
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
				if self.node.leftChild.node == None and self.node.rightChild.node == None:
					self.node = None
				# para apenas uma sub-arvore
				elif self.node.leftChild.node == None:
					self.node = self.node.rightChild.node
				elif self.node.rightChild.node == None:
					self.node = self.node.leftChild.node
				# para as duas sub-arvores cheias, deve-se encontrar um sucessor
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

			self.rebalance()
		else:
			return

	def find(self, value):
		if self.node != None:
			if self.node.value == value:
				return self.node
			elif value < self.node.value:
				self.node.leftChild.find(value)
			elif value > self.node.value:
				self.node.rightChild.find(value)
		else:
			return

	def print(self, level=0, pref='#'):
		#Atualizandoas heights antes de balancear
		self.update_heights()
		self.update_balances()
		if (self.node != None):
			print('\t' * level * 2, pref, self.node.value, '$' if self.is_leaf() else ' ')
			if self.node.leftChild != None:
				self.node.rightChild.print(level + 1, 'R')
			if self.node.leftChild != None:
				self.node.leftChild.print(level + 1, 'L')


if __name__ == "__main__":
	a = AVLTree()
	list = [5,3,4,1,2,0]
	for i in list:
		a.insert(i)

	a.print()
	print("deleting: ", 1)
	print("deleting: ", 5)
	a.delete(1)
	a.delete(5)
	a.print()
	print("Input: ", list)
	for i in list:
		a.insert(i)
	a.print()
	print("deleting: ", 3)
	print("deleting: ", 4)
	a.delete(3)
	a.delete(4)
	a.print()
	print("is balanced:",a.check_balanced())
	print(a.find(2))