#큐 알고리즘을 이용하면 펠린드롭
#회문 : 앞으로 읽던 거꾸로 읽어도 같은 글자가 나오는 것
#ex) level, wow, pop
#한번 검사하는 명령문
#큐는 앞에서 데이터를 꺼내오는 것
#스택은 뒷쪽에서 데이터를 꺼내온다.

queue = []
stack = []

def pailindrome(string):
  for i in string:
    if i.isalpha(): #i가 알파벳인지 확인해주는 함수/알파벳이면 True 반환
      queue.append(i.lower())#영문자는 대소문자를 구별한다. 모두 대문자로 변경 : upper(),모두 소문자로 변경 : lower()
      stack.append(i.lower())
  #각각 저장했으니 비교!
  while queue: #queue에 문자가 남아있으면 반복함.
    if queue.pop(0) != stack.pop():
      print("문자가 다릅니다.")
      break
  print("같은 문자입니다.")

string = input()
pailindrome(string)