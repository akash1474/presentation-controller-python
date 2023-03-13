def pow(x,y=2):
	r=1
	for i in range(y):
		r=r*x
		return r


print(pow(2))
print(pow(3,5))