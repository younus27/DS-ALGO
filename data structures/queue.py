class queue:
	def __init__(self,max_):
		self.q=[]
		self.max_ = max_
	def insert(self,ele):
		if len(self.q)==self.max_:
			print("Queue Full... Element not inserted")
			return
		self.q.append(ele)

	def delete(self):
		if len(self.q)==0:
			print("Queue Empty")
			return
		return self.q.pop(0)
	def q_front(self):
		if len(self.q)==0:
			print("Queue Empty")
			return
		return self.q[0]

	def display(self):
		if len(self.q)==0:
			print("Queue Empty")
			return
		print(self.q)


q=queue(5)
q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)
q.display()


print(q.q_front())

q.insert(6)
q.display()

q.delete()
q.display()
q.delete()
q.display()
q.delete()
q.display()
q.delete()
q.display()
q.delete()
q.display()
q.delete()
q.display()