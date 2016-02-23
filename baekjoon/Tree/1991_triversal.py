"""
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.



예를 들어 위와 같은 이진 트리가 입력되면,

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
가 된다.

입력
첫째 줄에는 이진 트리의 노드의 개수 N(1≤N≤26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 영문자 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현된다.

출력
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

예제 입력  복사
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
예제 출력  복사
ABDCEFG
DBAECFG
DBEGFCA
"""
# A의 아스키 코드는 65

num = int(input())
tree_array = [[] for _ in range(num+1)]

for i in range(num):
    a, b, c = map(lambda x: ord(x)-64, input().split())  #인덱스 번호를 따기 위해 아스키코드 값으로 index 부여
    b = max(b, 0)  #양수로 변경
    c = max(c, 0)  #양수로 변경
    tree_array[a].append(b)
    tree_array[a].append(c)

def preOrder(n):  #전위 순회
    if n == 0:
        return 0
    print(chr(n+64),end ="")
    preOrder(tree_array[n][0])
    preOrder(tree_array[n][1])

def inOrder(n):   #중위 순회
    if n == 0:
        return 0
    inOrder(tree_array[n][0])
    print(chr(n+64),end ="")
    inOrder(tree_array[n][1])

def postOrder(n):  #후위 순회
    if n == 0:
        return 0
    postOrder(tree_array[n][0])
    postOrder(tree_array[n][1])
    print(chr(n+64),end ="")

preOrder(1)
print()
inOrder(1)
print()
postOrder(1)
