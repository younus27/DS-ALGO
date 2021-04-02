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
		# p.data = ele
		q = self.start
		while q.next != None:
			q = q.next
		q.next = p


	def insert_beg(self,ele):
		p=node(ele)
		p.next = self.start
		self.start = p


	def insert_pos(self,ele,pos):
		if pos ==0:
			return
		if pos==1:
			self.insert_beg(ele)
			return
		if pos==2 and self.start.next!=None:
			p = node(ele)
			p.next = self.start.next
			self.start.next = p
			return

		p=node(ele)
		q=self.start
		try:
			for i in range(pos-2):
				q=q.next
			p.next = q.next
			q.next = p
		except:
			print("Invalid Position")
		return



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

	def delete_beg(self):
		if self.start.data == None:
			print("Empty LL")
			return
		self.start = self.start.next


	def delete_ele(self,ele):
		if self.start.data == None:
			print("Empty LL")
			return
		if self.start.data == ele:
			self.start = self.start.next

		q = self.start
		while q.next != None:
			if ele == q.next.data:
				break
			else:
				q = q.next
		if q.next ==None:
			print("Element not found")
			return
		q.next = q.next.next 


	def delete_pos(self,pos):
		if pos ==0:
			return
		if pos==1:
			self.delete_beg()
			return
		if pos==2 and self.start.next!=None:
			self.start.next = self.start.next.next
			return
		q=self.start
		try:
			for i in range(pos-2):
				q=q.next
			q.next = q.next.next
		except:
			print("Invalid Position")
		return



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
# ll.insert_beg(8)
ll.display()
# ll.delete()
# ll.display()
# ll.delete_beg()
# ll.display()
# ll.delete_ele(5)
# ll.display()


# ll.insert_pos(9,2)
# ll.display()
# ll.delete_pos(6)
# ll.display()

