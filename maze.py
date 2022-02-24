# 미로 찾기
# 딕셔너리를 이용해서 일단 저장
# 미로의 길이 어떻게 되어있는지 알아야된다.
# 미로의 각 위치에 알파벳으로 이름을 지정
# 각 위치에서 한 번에 이동할 수 있는 모든 위치를 선으로 연결하는 그래프 표현

maze = {
  'a' : ['e'],
  'e' : ['a', 'i'],
  'i' : ['e','m'],
  'm' : ['i','n'],
  'n' : ['m','j'],
  'j' : ['n', 'f','k'],
  'f' : ['j','b','g'],
  'k' : ['j','o'],
  'o' : ['k'],
  'g' : ['f','h'],
  'h' : ['g','l'],
  'l' : ['h','p'],
  'p' : ['l'],
  'b' : ['f','c'],
  'c' : ['b','d'],
  'd' : ['c'],
}
# info = 미로 정보
# start = 시작점
# fin = 도착점

def in_out(info, start, fin):
  queue = [] # 기억장소1 : 앞으로 처리해야할 이동 경로를 큐에 저장
  done = set() # 기억장소2 : 이미 큐에 추가한 꼭짓점들을 집합에 기록, set()은 중복을 삭제해줌.
  queue.append(start) # 출발점을 큐에 얺고 시작
  done.add(start) #set()에 추가할 때 add 쓰임.

  while queue : #큐가 처리할 데이터가 있으면
    p = queue.pop(0) # 가장 앞쪽에 위치한 데이터를 꺼내온다.
    v = p[-1] # 큐에 저장된 이동 경로의 마지막 문자가 현재 처리해야할 꼭짓점
    if v == fin: # end와 v값이 같다면 목적지에 도착!
      return p # 지금까지의 전체 이동경로를 돌려주고 종료
    for i in maze[v]: # 연결된 꼭짓점들 중에
      if i not in done: # 아직 큐에 추가된 적이 없는 꼭짓점을
        queue.append(p+i)
        done.add(i)
        # 탐색을 마칠 때까지 도착점이 나오지 않으면 나갈 수 없는 미로
  return '?'
# 변수 in 리스트,set(집합),딕셔너리,튜플
#  변수가 여러개를 저장하는 자료형안에 있니?
#  있으면 참 없으면 거짓
# not in : 변수가 여러개를 저장하는 자료형 안에 없니?
# 있으면 참, 없으면 거짓
print(in_out(maze,'a','p'))