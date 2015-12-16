#-*- coding: utf-8 -*-

x = lambda a, b : a+b
print x(10, 15)

array1 = [1, 2, 3, 4, 5, 6, 7]
array2 = [4, 5, 6, 7, 8, 9, 10] 
array3 = [10, 3, 15, 233, 30, 2]
array4 = [('a', 10), ('b', 30), ('z', 3), ('d', 8)]

x = lambda array1, array2 : array1+array2
print x(array1, array2)

x = lambda x: (x[0], -x[1]) # 인자1, 인자2, 인자3, 표현식 
print x(array1)

print sorted(array4, key =lambda x: (x[1]))
# print array3

items = [(0, 'a'), (0, 'B'), (1, 'A'), (1, 'B'), (2, 'A')]
# print sorted(array4, key=lambda x: (x[0], x[1]))

x = map(lambda x : x**2, array1)  # map(함수 , 리스트)
print x

array = [-1, 3, -4, 10, 5, 7]
print sorted(array, key = lambda x : x**2)
 
def sum(a, b):
	return a+b

x = lambda a, b: a+b


def square(n):
	return n**2

new_array = map(square, range(10))

arr = [-2, 1, 5, 9, 13]
new_arr = map(lambda x: x+10, arr)
print new_arr


