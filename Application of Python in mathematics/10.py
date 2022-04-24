data = [1,2,3,4,5,6,7,8,9]

def count(data) :
	c=0 
	for i in data :
		c += 1 
	return c

def sum(data) :
	s=0
	for i in data :
		s += i 
	return s
	
def mean(data) :
	return sum(data) / count(data)

print("mean:", mean(data))