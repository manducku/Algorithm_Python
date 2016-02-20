"""
피보나치 함수
문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	11967	3666	2836	34.489%
문제
다음 소스는 N번째 피보나치 함수를 구하는 함수이다.

1
2
3
4
5
6
7
8
9
10
11
int fibonacci(int n) {
    if (n==0) {
        printf("0");
        return 0;
    } else if (n==1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.

fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.

두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.

fibonacci(0)은 0을 출력하고, 0을 리턴한다.

fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.

첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.

fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.

이 때, 1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 구성되어있다.

첫째 줄에 N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

출력
각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.

예제 입력  복사
3
0
1
3
예제 출력  복사
1 0
0 1
1 2
"""

n = int(input())



for _ in range(n):
    m = int(input())

    count_zero = 0
    count_one = 0
    memo = [0]*(m+1)
    memo[1] = 1

    def fibo(n):
        global count_zero, count_one
        if n == 0:
            count_zero += 1
            return 0
        elif n == 1:
            count_one += 1
            return 1
        elif(memo[n] > 0):
            return memo[n]
        else:
            memo[n] = fibo(n-1)+fibo(n-2)
            return memo[n]

    fibo(m)
    print(count_zero, count_one)
    print(memo)
    count_one, count_zero = 0, 0
