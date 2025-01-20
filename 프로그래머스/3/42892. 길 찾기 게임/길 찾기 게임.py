import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, idx, x, y):
        self.idx = idx
        self.x = x
        self.y = y
        self.left = None
        self.right = None

def solution(nodeinfo):
    # 노드 번호와 좌표를 묶어서 정렬
    nodes = []
    for idx, (x, y) in enumerate(nodeinfo):
        nodes.append((idx + 1, x, y))  # 각 노드에 번호를 붙임 (idx + 1)
    
    # y 값 기준 내림차순, x 값 기준 오름차순으로 정렬
    nodes.sort(key=lambda x: (-x[2], x[1]))
    
    # 이진 트리 구성
    root = build_tree(nodes)
    
    # 전위 순회와 후위 순회
    preorder_result = []
    postorder_result = []
    
    def preorder(node):
        if node is None:
            return
        preorder_result.append(node.idx)
        preorder(node.left)
        preorder(node.right)
    
    def postorder(node):
        if node is None:
            return
        postorder(node.left)
        postorder(node.right)
        postorder_result.append(node.idx)
    
    preorder(root)
    postorder(root)
    
    return [preorder_result, postorder_result]

def build_tree(nodes):
    if not nodes:
        return None
    
    idx, x, y = nodes[0]  # 첫 번째 노드로 루트를 만듦
    root = Node(idx, x, y)
    
    # 왼쪽 서브트리 노드 (x가 root보다 작은 값들)
    left_nodes = []
    for node in nodes[1:]:
        if node[1] < x:
            left_nodes.append(node)
    
    # 오른쪽 서브트리 노드 (x가 root보다 큰 값들)
    right_nodes = []
    for node in nodes[1:]:
        if node[1] > x:
            right_nodes.append(node)
    
    # 재귀적으로 왼쪽, 오른쪽 서브트리 구축
    root.left = build_tree(left_nodes)
    root.right = build_tree(right_nodes)
    
    return root