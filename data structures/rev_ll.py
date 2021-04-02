class node:
	def __init__(self,data = None,next_ = None):
		self.data = data
		self.next = next_
class linkedList:
	def __init__(self):
		self.start = node()

	def insert(self,ele):
		if self.start.data == None:
			self.start.data = ele
			return
		p = node(ele)
		q = self.start
		while q.next != None:
			q = q.next
		q.next = p


	def rev(self):
		prev = None
		curr = self.start
		while curr !=None:
			next_ = curr.next

			curr.next = prev
			prev = curr
			curr = next_ 
		self.start = prev


	def display(self):
		ll=[]
		q = self.start
		while q:
			ll.append(q.data)
			q = q.next
		print(ll)


ll=linkedList()
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.insert(8)
ll.display()

ll.rev()
ll.display()

ll.insert(9)
ll.display()



#