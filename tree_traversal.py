"""
트리 순회
트리 안에 있는 데이터에 접근하는 방식
1. 전위 순회(가장 많이 쓰이는 방식) : 루트->왼쪽->더 이상 데이터가 없으면 오른쪽
2. 중위 순회 : 왼쪽->루트->오른쪽
3. 후위 순회 : 왼쪽->오른쪽->노드

class TreeNode:
  def __init__(self,data=None, left = None, right = None):
    self.data = data # 만든 객체에 데이터가 있으면 그 데이터 값을 가져오고 없으면 None으로 저장
    self.left = left # 왼쪽 주소
    self.right = right # 오른쪽 주소
"""
class TreeNode:
  def __init__(self,data=None):
    self.data = data # 만든 객체에 데이터가 있으면 그 데이터 값을 가져오고 없으면 None으로 저장
    self.left = None # 왼쪽 주소
    self.right = None # 오른쪽 주소

# 객체 생성
node1 = TreeNode('Chandler') # Chandler가 루트
node2 = TreeNode('Ross') 
node1.left = node2 # Chandler의 왼쪽에는 Ross
node3 = TreeNode('Joey') 
node1.right = node3  # Chandler의 오른쪽에는 Joey
node4 = TreeNode('Monica')
node2.left = node4 #Ross의 왼쪽에는 Monica
node5 = TreeNode('Rachel')
node2.right = node5 #Ross의 오른쪽에는 Rachel
node6 = TreeNode('Pheobe')
node3.left = node6 # Joey의 왼쪽에는 Phoebe

# 전위순회
def preorder(node):
  if node == None: #not(!) 연산자를 쓰면 
    return
  
  preorder(node.left) # 전위순회는 무조건! 왼쪽에 데이터가 있는지 확인
  preorder(node.right)

print(preorder(node1))