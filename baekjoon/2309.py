"""
일곱 난쟁이
문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	1979	1028	875	54.756%
문제
왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.

아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.

입력
아홉 개의 줄에 걸쳐 일곱 난쟁이의 키가 주어진다. 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 항상 답이 유일한 경우만이 입력으로 주어진다고 가정해도 좋다.

출력
일곱 난쟁이의 키를 오름차순으로 출력한다.

예제 입력  복사
20
7
23
19
10
15
25
8
13
예제 출력  복사
7
8
10
13
19
20
23
"""

li = []
for i in range(9):
    li.append(int(input()))

total = sum(li)
li.sort()


for i in range(8):
    for j in range(i+1, 9):
        if((total-li[i]-li[j]) == 100):
            result1 = i
            result2 = j

for i in range(9):
    if(i == result1 or i == result2):
        continue
    else:
        print(li[i])




