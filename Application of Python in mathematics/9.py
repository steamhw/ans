data = [1,2,3,4,5,6,7,8,9]

def count(data) :
	c=0 
	for i in data :
		c += 1 
	return c

print("count:", count(data))