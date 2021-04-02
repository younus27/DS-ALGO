def insertion_sort(x,n):
	for i in range(0,n-1):
		value = x[i+1]

		j=i
		for j in range(i,-2,-1):
			if x[j] > value:
				x[j+1] = x[j]
			else:
				break
		x[j+1] = value
		print(x)
	return x


arr  = [6,5,4,3,2,1]
print(arr)
print(insertion_sort(arr,len(arr)))
