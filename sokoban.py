""""
소코반 게임을 구현해보자.
플레이어의 시작 위치를 입력받고 아래 규칙대로 움직이는 내용을 작성
벽이 몇 개인가
플레이어의 위치(입력을 받던가, 랜덤으로 할당받던지)
위 아래 오른쪽 왼쪽(숫자로 표시하자 1,2,3,4)
맵의 사이즈는 7x7 2차원 리스트로 표현
사용자로부터 벽의 설치 개수를 물어 랜덤한 위치에 설치
공과 골대를 벽과 겹치지 않도록 랜덤한 위치에 설치
플레이어는 상하좌우로 이동이 가능하다.
움직여서 골대까지 가는 움직임을 스택, 큐, 그래프 이용해서 저장
랜덤 라이브러리를 가져오자.
"""

#import random # 랜덤파일이 어디 있는지 위치만 알려줌.
              # random.randint()을 써야 실행됨.
from random import* # *는 전부 다 가져오라는 뜻
                    # randint()만 써도 실행됨.
# map 생성
map = [['0']*7 for i in range(7)]

#map 사이즈
map_size = 7
player = 2 # 플리에이어
ball = 3 # 공
goal = 7 # 골대
wall = 9 # 벽

# 벽이 몇개 있는지 저장
wall_count = 0
# 플레이어의 위치 저장
player_x = 0 # x좌표
player_y = 0 # y좌표

# 공의 위치, 골대의 위치 각각 저장
ball_x = 0 # x좌표
ball_y = 0 # y좌표

goal_x = 0 # x좌표
goal_y = 0 # y좌표

# 벽 설치
wall_count = int(input('벽을 몇 개 설치하시겠습니까?'))

while wall_count != 0:
  #벽이 한개 이상이면 벽을 설치할 랜덤값을 뽑아야된다.
  rand_x = randint(0, map_size-1)
  rand_y = randint(0, map_size-1)
  map[rand_x][rand_y] = wall
  wall_count -= 1

# 공 설치
# 랜덤한 위치에 행, 열 위치 잡아주고 
# 볼 현재 위치를 ball_x, ball_y 에 저장
# 주의 : 벽이 있는 곳에는 공을 놓을 수 없다.
while True:
  
  rand_x = randint(0, map_size-1)
  rand_y = randint(0, map_size-1)
  
  if map[rand_x][rand_y] == '0':
    map[rand_x][rand_y] = ball
    ball_x = rand_x # x좌표
    ball_y = rand_y # y좌표
    break
    
# 골대 설치
while True:
  
  rand_x = randint(0, map_size-1)
  rand_y = randint(0, map_size-1)
  
  if map[rand_x][rand_y] == '0':
    map[rand_x][rand_y] = goal
    goal_x = rand_x # x좌표
    goal_y = rand_y # y좌표
    break

# 플레이어 위치 설치
while True:
  
  rand_x = randint(0, map_size-1)
  rand_y = randint(0, map_size-1)
  
  if map[rand_x][rand_y] == '0':
    map[rand_x][rand_y] = player
    player_x = rand_x # x좌표
    player_y = rand_y # y좌표
    break

# 맵 출력
while True:
  i = 0
  while i<map_size: # i는 행을 반복
    k = 0
    while k <map_size: # k는 열을 반복
      print(map[i][k], end = '')
      k+=1
    print()
    i+=1
  
  # 게임 종료
  if goal_x == ball_x and goal_y == ball_y:
    print('게임 종료')
    break

  move = int(input('상(1) 하(2) 좌(3) 우(4):'))
# 혹시 주인공의 위치가 변경 
  xx = player_x
  yy = player_y

    # 이동
  if move == 1:               # 위쪽으로 이동
    yy = yy -1
  elif move == 2:
    yy = yy +1

  elif move == 3:
    xx = xx -1

  elif move == 4:
    xx = xx +1

    # 예외처리 ( 왼쪽 오른쪽 튀여나가지 않게 하는 명령문)
  if map_size <= xx and xx < 0:
    continue 

  if map_size <= yy and yy < 0: #( 위쪽 오른쪽 끝으로 튀어나지 않는 명령문)
    continue

  if map[yy][xx] != 0 and map[yy][xx] != ball:
    continue

    #공을 만나면
  if map[yy][xx] == ball:
    # 골을 끌고 골대로 이동 위 아래 좌 우
    yyy = yy
    xxx = xx

    if move == 1: # 위쪽으로 이동
      yy = yy -1
    elif move == 2:
      yy = yy +1

    elif move == 3:
      xx = xx -1

    elif move == 4:
      xx = xx +1

    if map_size <= xx and xx < 0:
      continue 

    if map_size <= yy and yy < 0: #( 위쪽 오른쪽 끝으로 튀어나지 않는 명령문)
      continue

    if map[yyy][xxx] != 0 and map[yyy][xxx] != goal:
      continue

    map[ball_y][ball_x] = 0
    ball_y = yyy
    ball_x = xxx
    map[ball_y][ball_x] = ball

  # 캐릭터 이동
  map[player_y][player_x] = 0
  player_y = yy
  player_x = xx
  map[player_y][player_x] = player

# player지나간 위치를 스택에 저장   

class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.next = 0       # 스택을 연결하는 값을 저장(주소)
        
class Stack:
    def __init__(self,data):
        self.data = data
        self.top = 0        # 스택에 가장 마지막 노드를 가리킨다.

    def push(self):
        # 노드를 생성하고 player움직인 위치를 각각 저장 
        pass
        
    def pop(self):
        # 잘 못 간 위치는 빼고 골대까지 가는 최소 경로를 저장 
        pass 

# from collects import deque
# 큐 구조로 내가 저장(pop(0))
# 스택구조로 내가 저장 (pop())