#-*- coding: utf-8 -*-

def matrixMultiple(a, b):

	c = [[ 0 for i in range(len(b[0]))] for j in range(len(a))]  #리스트 내에 for문을 내포하는 방법 
	
	for i in range(len(a)):  #a 행렬의 행번호
		for j in range(len(b[0])): # b 행렬의 열번호 
			for k in range(len(a[i])): # a행렬의 열번호 
				c[i][j] += a[i][k] * b[k][j]

	return c

def squareMatrix(a, n):
	c = [[ 0 for i in range(len(a))] for j in range(len(a))]
	c = a

	for i in range(n-1):
		c = matrixMultiple(c, a)

	return c

def sqMatrix(a, n):

	if n == 1:
		return a
	elif (n%2 == 1):
		return matrixMultiple(sqMatrix(a, n-1), a)
	
	half = sqMatrix(a, n/2)
	return matrixMultiple(half, half)



def main():
	a = [[1,1,1] for i in range(3)]
	b = [[1,1] for i in range(2)]

	#print(matrixMultiple(a, b))
	print(squareMatrix(b, 4))
	print(sqMatrix(b, 4))

if __name__ == '__main__':
	main()	