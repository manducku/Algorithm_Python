#-*- coding: utf-8 -*-

#loc_str = raw_input("위치를 입력하세요.")
#listOfloc = map(int, loc_str.split())

listOfloc = [1, 3, 4, 8, 13, 17, 20]
pair = zip(listOfloc[0:], listOfloc[1:])
pair.sort(key= lambda x : x[1]- x[0])

print pair[0]