class stack: 
	def __init__(self):
		self.stack = []

	def push(self,ele):
		self.stack.append(ele)

	def pop(self):
		if len(self.stack)==0:
			print('Stack Empty')
			return 
		return self.stack.pop(-1)

	def stacktop(self):
		if len(self.stack)==0:
			print('Stack Empty')
			return
		return self.stack[-1]

	def diplay(self):
		if len(self.stack)==0:
			print('Stack Empty')
			return
		return self.stack
s=stack()
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
print(s.diplay())
s.pop()
print(s.diplay())
s.pop()
print(s.diplay())
s.pop()
print(s.diplay())
s.pop()
print(s.diplay())
s.pop()
print(s.diplay())

# print(s.stacktop())