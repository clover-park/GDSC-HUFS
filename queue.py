"""
큐 : 먼저 들어간 데이터가 먼저 나가는 구조
FIFO(first in first out)
ex) 대기줄, 번호표
큐에 데이터 추가 : enqueue
큐에서 데이터를 꺼내기 : dequeue
큐 앞 쪽에 항목을 조회 : front
큐의 마지말 데이터 : rear
"""
class Queue:
    def __init__(self):     # 큐 생성
        self.items = []

    def enqueue(self,item):   #  큐 추가
        self.items.append(item)

    def dequeue(self):            #큐 삭제
        return self.items.pop(0)

    def front(self):    # 가장 앞에 있는 항목 조회
        return self.items[0]

    def isEmpty(self):   # 큐 비었는지 확인(비었으면True, 데이터 들어있다.False)
        return not self.items

# 큐 객체 생성
que = Queue()

que.enqueue(10)
que.enqueue(20)

print(que.items)
# 삭제
print(que.dequeue())
print(que.items)

# 비었는지 확인
print(que.isEmpty())

#큐 알고리즘을 이용하면 펠린드롭
#회문 : 앞으로 읽던 거꾸로 읽어도 같은 글자가 나오는 것
#ex) level, wow, pop
#한번 검사하는 명령문
#큐는 앞에서 데이터를 꺼내오는 것
#스택은 뒷쪽에서 데이터를 꺼내온다.

queue = []
stack = []
#문자열의 알파벳을 각각 큐와 스택에 저장
string = 'WOw' #영문자는 대소문자를 구별한다. 모두 대문자로 변경 : upper(),모두 소문자로 변경 : lower()

for i in string:
  if i.isalpha(): #i가 알파벳인지 확인해주는 함수
    queue.append(i.lower())
    stack.append(i.lower())