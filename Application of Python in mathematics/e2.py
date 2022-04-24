import math

def triangle_length(b, c, A):
	return math.sqrt(math.pow(b,2)+math.pow(c,2)-2*b*c*math.cos(math.radians(A)))

print(triangle_length(10,9,47))