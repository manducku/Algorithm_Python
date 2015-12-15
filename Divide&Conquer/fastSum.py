def fastSum(n):

	if n == 1:
		return 1

	elif(n%2 == 1):
		return fastSum(n-1) + n

	else:
		return (n*n)/4 + 2*fastSum(n/2)

def main():
	print(fastSum(10))

if __name__ == '__main__':
	main()