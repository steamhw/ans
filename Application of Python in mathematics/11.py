data = [1,2,3,4,5,6,7,8,9]

def median(data) :
	m = count(data) / 2 
	m = int(m) 
	data.sort() 
	return data[m]

print("median:", median(data))