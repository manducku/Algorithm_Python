"""
1로 만들기
문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	3466	953	694	30.122%
문제
세준이는 어떤 정수 N에 다음과 같은 연산중 하나를 할 수 있다.

N이 3으로 나누어 떨어지면, 3으로 나눈다.
N이 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
세준이는 어떤 정수 N에 위와 같은 연산을 선택해서 1을 만드려고 한다. 연산을 사용하는 횟수의 최소값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 10^6보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최소값을 출력한다.

예제 입력  복사
2
예제 출력  복사
1
"""

n = int(input())
d = [0] * (n+1)
d1 = [0] * (n+1)

#D[N] = MAX(D[N/3] + D[N/2] + D[N-1])

for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if(i%3 == 0 and d[i] > d[i//3]+1):
        d[i] = d[i//3] + 1
    if(i%2 == 0 and d[i] > d[i//2]+1):
       d[i] = d[i//2] + 1

print (d[n])


def dyn(n):

    if(n == 1):
        return 0
    if(d1[n] > 0):
        return d1[n]

    d1[n] = dyn(n-1)+1
    if(n%3 == 0):
        temp = dyn(n//3) + 1
        if(temp < d1[n]):
            d1[n] = temp
    if(n%2 == 0):
        temp = dyn(n//2) + 1
        if(temp < d1[n]):
            d1[n] = temp

    return d1[n]

print (dyn(n))
