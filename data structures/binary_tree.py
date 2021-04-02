class node:
	def __init__(self,data,left=None,right=None):
		self.left  = left
		self.right = right
		self.data  = data
	def display(self):
		if self.left:
			self.left.display()
		print(self.data)
		if self.right:
			self.right.display()

	def insert(self,data):
		if self.data:
			if data<self.data:
				if self.left is None:
					self.left = node(data)
				else:
					self.left.insert(data)
			elif data>self.data:
				if self.right is None:
					self.right = node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data
	def next(self,data,l=[]):
		if self.left:
			self.left.next(data,l)
		l.append(self.data)
		if self.right:
			self.right.next(data,l)
		try:
			return l[l.index(data)+1]
		except:
			return -1
	def search(self,data):
		if data<self.data:
			if self.left is None:
				return str(data)+" NOT Found"
			return self.left.search(data)

		elif data> self.data:
			if self.right is None:
				return str(data)+" NOT Found"
			return self.right.search(data)

		else:
			return str(data)+" Found"
			


root = node(10)

root.insert(6)
root.insert(14)
root.insert(3)
root.insert(20)
root.insert(1)
root.insert(12)
root.display()

# print("\n\n",root.next(1))
print("\n\n",root.search(11))