#-*- coding: utf-8 -*-

m = input("총 건수? ")
n = input("한 페이지에 보여줄 게시물 수? ")

if n == 0:
	print("잘못된 입력입니다. ")

print ("총페이지수는 ? %d" %(m/n))

