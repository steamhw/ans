

class Statistics :
	def __init__(self) :
		self.data = [] 

	def append(self, data) :
		self.data.append(data)

	def min(self) :
		self.data.sort()
		return self.data[0]

	def max(self) :
		self.data.sort(reverse = True)
		return self.data[0]

	def count(self) :
		c=0
		for i in self.data :
			c += 1
		return c

	def sum(self) :
		s=0
		for i in self.data :
			s += i
		return s

	def mean(self) :
		return self.sum() / self.count()

	def median(self) :
		self.data.sort()
		m = self.count() / 2 
		m = int(m) 
		return self.data[m]

s = Statistics()
s.append(1)
s.append(2)
s.append(3)
print(s.min())
print(s.max())
print(s.sum())
print(s.count())
print(s.median())
print(s.mean())