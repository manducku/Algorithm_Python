#-*- coding: utf-8 -*-

def calArea(fenceList):
	result = 0

	for st1 in range(len(fenceList)-1):
		height = fenceList[st1]
		width = 1
		temp = height

		for st2 in range(st1+1, len(fenceList)):
			if fenceList[st1] <= fenceList[st2]:
				width = width+1
				continue
			else:
				break

		if(st1 > 0):
			for st3 in range(st1-1, -1, -1):
				if fenceList[st1] <= fenceList[st3]:
					width = width+1
					continue
				else:
					break

		temp = width * height
		result = max(temp, result)

	return result




def main():

	testNum = input()

	for i in range(testNum):
	 	fenceList = []
	 	fenceNum = input()
	 	st = raw_input()

	 	for i in range(len(st)):
	 		if st != " ":
	 			fenceList.append(st[i])

		print(calArea(fenceList)) 	

	
if __name__ == '__main__':
	main()	

