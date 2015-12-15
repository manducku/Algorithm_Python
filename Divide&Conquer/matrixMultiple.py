#-*- coding: utf-8 -*-

def matrixMultiple(a, b):

	c = [[ 0 for i in range(len(b[0]))] for j in range(len(a))]  #리스트 내에 for문을 내포하는 방법 
	
	for i in range(len(a)):  #a 행렬의 행번호
		for j in range(len(b[0])): # b 행렬의 열번호 
			for k in range(len(a[i])): # a행렬의 열번호 
				c[i][j] += a[i][k] * b[k][j]

	return c

def main():
	a = [[1,1,1] for i in range(3)]
	b = [[1,1] for i in range(3)]

	print(matrixMultiple(a, b))

if __name__ == '__main__':
	main()	