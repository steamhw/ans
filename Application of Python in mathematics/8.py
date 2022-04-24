data = [1,2,3,4,5,6,7,8,9]

def sum(data) :
	s=0
	for i in data :
		s += i 
	return s

print("sum:", sum(data))