#-*- coding: utf-8 -*-

loc_str = raw_input("위치를 입력하세요.")

listOfloc = map(int, loc_str.split())
listOfdis = list()
result = 99999

for i in range(len(listOfloc)-1):
	temp = listOfloc[i+1] - listOfloc[i]

	if result > temp:
		result = temp
		lastIndex = i

print listOfloc[lastIndex], listOfloc[lastIndex+1]


