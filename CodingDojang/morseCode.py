
morseDic = { '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',   # morse부호를 저장하는 dictionary 
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'}

lines = raw_input()  # 라인을 입력 받음  
morseList = lines.split(" ")
result = []

for morse in morseList:
	if morse == "":
		result.append(" ")  # 공백을 표현하는 방법 
	 	continue
	else:
	 	result.append(morseDic[morse])

print "".join(result) ##list를 string으로 변환하는 방법 
