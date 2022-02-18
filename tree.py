"""
트리
루트 노드(root node) : 기준점, 부모가 없는 노드, 하나의 루트 노드만 가진다.
단말 노드 : 자식이 없는 노드
간선 : 노드를 연결하는 선
형제 : 같은 부모를 가지는 노드
크기 : 자기를 포함한 모든 자손 노드의 개수
깊이 : 루트에서 어떤 노드에 도달하기 위해서 거쳐야 하는 간선의 수
레벨 : 트리의 특정 깊이를 가지는 노드의 집합
노드의 차수 : 하위 트리의 개수/간선 수 = 각 노드가 지닌 가지의 수

이진트리
"""
class TreeNode:
  def __init__(self, data):
    self.data = None
    self.left = None
    self.right = None

# 트리노드를 이용해서 데이터를 생성

node1 = TreeNode(10)
node2 = TreeNode(20)
node3 = TreeNode(30)

# 기준은 node2로 해보자

node2.right = node1
node2.left = node3

print(node2.left.data)