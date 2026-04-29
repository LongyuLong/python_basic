# Binary Tree(이진트리) : 자식이 둘 히아 (차수가 2이하)인 노드로 구성된 트리
# 노드 방문 방법 3가지 : pre-order(전위), in-order(중위), post-order(후위)
# 
tree = {
    'A':('B','C'),
    'B':('D','E'),
    'C':(None, None),
    'D':(None, None),
    'E ':(None, None)
}

# 전위순회
def preOrder(node) :
    if node is None :
        return
    print(node, end=' ')
    left, right = tree[node]
    preOrder(left)      # 재귀
    preOrder(right)

# 중위순회
def preOrder(node) :
    if node is None :
        return
    print(node, end=' ')
    left, right = tree[node]
    preOrder(left)      # 재귀
    print(node, end=' ') 
    preOrder(right)
    
# 후위순회
def preOrder(node) :
    if node is None :
        return
    print(node, end=' ')
    left, right = tree[node]
    preOrder(left)      # 재귀
    preOrder(right)
    print(node, end=' ') 

print('전위 순회 결과 : ')
preOrder('A')
print('전위 순회 결과 : ')
preOrder('A')   # BST(Binary Search Tree) 오름차순 정렬 가능
print('전위 순회 결과 : ')
preOrder('A')