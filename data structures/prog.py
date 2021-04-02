
# def fibbo(n):
# 	a,b = 0,1
# 	sum = 0
# 	count = 1
# 	while(count <= n):
# 	  print(sum,end = ' ')
# 	  count += 1
# 	  a = b
# 	  b = sum
# 	  sum = a + b

# fibbo(1)
# print()

# 1  
# 1 1 
# 1 2 1 
# 1 3 3 1 
# 1 4 6 4 1 
# 1 5 10 10 5 1 


def list_to_str(l):
	s=""
	for i in range(len(l)):
		s+=str(l[i]) +", "
	return s[:-2]



def pascal(n):
	if n==1:
		return [1]
	final=[[1],[1,1]]
	if n==2 :
		return final
	
	for i in range(1,n):
		l= final[i]
		temp=[]
		for i in range(len(l)-1):
			temp.append(l[i]+l[i+1])
		temp.insert(0,1)
		temp.append(1)
		final.append(temp)
	return final

l = pascal(5)
for i in range(len(l)):
	print(list_to_str(l[i]))


