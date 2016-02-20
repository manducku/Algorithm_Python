"""
DFS와 BFS 실패
문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
5 초	128 MB	5034	1424	900	27.256%
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.

입력
첫째 줄에 정점의 개수 N(1≤N≤1,000), 간선의 개수 M(1≤M≤10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 한 간선이 여러 번 주어질 수도 있는데, 간선이 하나만 있는 것으로 생각하면 된다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력  복사
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력  복사
1 2 4 3
1 2 3 4
"""

v,e,start = map(int, input().split())
adj = [[0 for i in range(v+1)] for i in range(v+1)]


for _ in range(e):
    e1, e2 = map(int,input().split())
    adj[e1][e2] = adj[e2][e1] = 1

visited_DFS = [0 for _ in range(v+1)]
st = [start]
dfs =[]
bfs = []

while(st):
    now = st.pop()

    if(visited_DFS[now] == 0):
        dfs.append(now)
        visited_DFS[now] = 1

    for i in range(v, 0, -1):
        if(adj[now][i] == 1 and visited_DFS[i] == 0):
            st.append(i)

q = [start]
visited_BFS = [0 for _ in range(v+1)]

while(q):
    now = q.pop(0)
    if(now == start):
        visited_BFS[now] = 1
        bfs.append(now)

    for i in range(v+1):
        if(adj[now][i] == 1 and visited_BFS[i] == 0):
            q.append(i)
            visited_BFS[i] = 1
            bfs.append(i)

print(" ".join(map(str, dfs)))
print(" ".join(map(str, bfs)))

visited_Recursive = [0 for _ in range(v+1)]

def dfs(now):
    visited_Recursive[now] = 1
    print(now , end = ' ')
    for i in range(1, v+1):
        if(adj[now][i] == 1 and visited_Recursive[i] == 0):
            dfs(i)
dfs(1)




