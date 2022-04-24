import math

def compound_interest(principal, rate, years):
	return principal*math.pow((1+rate/100), years)

print(compound_interest(10,3,5))