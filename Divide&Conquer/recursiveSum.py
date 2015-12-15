def sum(n):

	if n == 1:
		return 1

	else:
		return sum(n-1) + n

def main():
	print sum(10)


if __name__ == '__main__':
	main()
