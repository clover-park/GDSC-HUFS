from collections import deque

def BFS(graph, start, visited):
  queue = deque([start])
  # 현재 노드를 방문 처리
  visited[start] = True

  while queue: #큐가 빌때까지 반복
    #큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end = '')
    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 쿠에 삽입

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5]
]
# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트로)
visited = [False]*5
BFS(graph, 1, visited)