# 탐색 
#  순차 탐색 ( 순서대로 앞에 부터 데이터를 찾아간다)

list1 = [17,92,18,33,58,7,32]

# 리스트에서 특정 숫자의 위치를 찾는다.
# 입력: 찾을 값
# 결과: 값이 있으면 그 값의 방 번호(위치,인덱스),찾지 못하면 -1

num = int(input('찾을 데이터>'))
size = len(list1)      # 리스트의 개수
print(size)

index = -1        # 만약에 데이터가 있으면 index 변경 없으면 그냥 -1

# 시작: 0
i = 0

while i < size:
    if list1[i] == num:
        index = i
        #print(num,'값은',i+1,'번째 있다')
        break
    i = i +1     #증가

if index != -1:
    print(num,'값은',index +1,'번째 있다')
else:
    print("찾는 데이터가 없다")