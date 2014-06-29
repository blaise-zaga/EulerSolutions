sum = 2

prev = 1
cur = 2

while(sum > 0):
	if(cur > 4000000): break
	temp = cur
	cur = prev + cur
	prev = temp
	
	if(cur % 2 == 0):
		sum  += cur
		
print sum
