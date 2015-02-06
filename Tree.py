# Binary Tree functions

class BinaryTree:
	def __init__(self,value):
		self.key=value
		self.left=None
		self.right=None

	def setLeft(self,value):
		if self.left==None:
			self.left=BinaryTree(value)
		else:
			t=BinaryTree(value)
			t.left=self.left
			self.left=t

	def setRight(self,value):
		if self.right==None:
			self.right=BinaryTree(value)
		else:
			t=BinaryTree(value)
			t.right=self.right
			self.right=t

	def getRoot(self):
		return self.key

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def setRoot(self,value):
		self.key=value



# Testing
r = BinaryTree('a')
print(r.getRoot())
print(r.getLeft())
r.setLeft('b')
print(r.getLeft())
print(r.getLeft().getRoot())
r.setRight('c')
print(r.getRight())
print(r.getRight().getRoot())
r.getRight().setRoot('hello')
print(r.getRight().getRoot())
