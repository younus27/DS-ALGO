#for i in range(n-2) 
#find minimum element, swap with x[i]

def selection_sort(x,n):
	for i in range(n-1):
		min_i = i
		for j in range(i+1,n):
			if x[j] < x[min_i]:
				min_i = j
		temp = x[i]
		x[i] = x[min_i]
		x[min_i] = temp
		print(x)
	return x

arr = [7,2,1,4,5,8,3]
print(arr)
print(selection_sort(arr,len(arr)))