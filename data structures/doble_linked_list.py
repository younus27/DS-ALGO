class node:
	def __init__(self,data = None,next_ = None,prev = None):
		self.data = data
		self.next = next_
		self.prev = prev
class linkedList:
	def __init__(self):
		self.start = node()
		self.last  = self.start

	def insert(self,ele):
		if self.start.data == None:
			self.start.data = ele
			return
		p = node(ele)
		# p.data = ele
		q = self.start
		while q.next != None:
			q = q.next
		q.next = p
		p.prev = q
		self.last = p


	def delete(self):
		if self.start.data == None:
			print("Empty LL")
			return
		if self.start.next == None:
			self.start = None
		q = self.start
		while q.next.next != None:
			q = q.next
		q.next = None
		q.prev = None

	def delete_ele(self,ele):
		if self.start.data == None:
			print("Empty LL")
			return

		if self.start.data == ele and self.last.prev.data != ele:
			if self.start == self.last:
				self.start = None
				self.last = None
			else:
				self.start = self.start.next
		if  self.last.prev.data == ele:
			self.last = self.last.prev
			self.last.next=None

		q = self.start
		while q.next != None:
			if ele == q.next.data:
				break
			else:
				q = q.next
		if q.next ==None:
			print("Element not found")
			return
		q.next.next.prev = q
		q.next = q.next.next 





	def display(self):
		ll=[]
		q = self.start
		while q:
			ll.append(q.data)
			q = q.next
		print(ll)

	def display_rev(self):
		ll=[]
		q = self.last
		while q:
			ll.append(q.data)
			q = q.prev
		print(ll)	




ll=linkedList()
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.insert(8)


ll.display()
ll.display_rev()
ll.delete_ele(5)