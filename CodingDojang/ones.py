
raw = input()
num = 1 
digit = 1

while True:
	if num%raw == 0:
		break
	else:
		num = num*10 + 1
		digit += 1

print digit
