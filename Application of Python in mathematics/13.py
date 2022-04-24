data = [1,2,3,4,5,6,7,8,9]

def max(data) :
	data.sort(reverse = True)
	return data[0]

print("max:", max(data))