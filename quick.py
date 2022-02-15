# 퀵정렬
#  기준을 하나 뽑은 다음에 작은 그룹과 큰 그룹
#   나중에 합치는 정렬 
#  재귀 함수 : 자기 자신을 호출하는 함수 (멈추는 기능)

list1 = [10,6,8,3,5,4,1,2,7,9]

def quick_sort(list1):
    n = len(list1)
    # 종료조건:  정렬할 리스트의 값의 개수가 한개 이하이면 정렬할 필요가 없음
    if n <=1:
        return list1

    pivot = list1[-1]  # 가장 오른쪽에 있는 값 ( 마지막 값)

    leftArr, rightArr = [],[]

    for i in range(0,n-1):    # 맨 마지막이 기준 마지막 방번호는 범위에 포함X
        if list1[i] < pivot:
            leftArr.append(list1[i])

        else:
            rightArr.append(list1[i])

    print('왼쪽:',leftArr)
    print('오른쪽:',rightArr)
    
    # 리스트 연결 가능 하다 
    return quick_sort(leftArr) + [pivot] + quick_sort(rightArr)

res = quick_sort(list1)
print(res)

'''
def quick_sort(list1):
    n = len(list1)
    # 종료조건:  정렬할 리스트의 값의 개수가 한개 이하이면 정렬할 필요가 없음
    if n <=1:
        return list1

    pivot = list1[n // 2]    # 중간값을 지정 
    #pivot = a[-1]  # 가장 오른쪽에 있는 값 ( 마지막 값)

    leftArr, rightArr = [],[]

    for i in list1:
        if i < pivot:
            leftArr.append(i)

        elif i > pivot :
            rightArr.append(i)

    print('왼쪽:',leftArr)
    print('오른쪽:',rightArr)
    
    # 리스트 연결 가능 하다 
    return quick_sort(leftArr) + [pivot] + quick_sort(rightArr)
'''
class Stu:
    def __init__(self,hak,score):
        self.hak = hak
        self.score = score


stulist = []

while True:
    print('1. 추가 2. 정렬 3. 순위표 0.종료')

    cho = int(input('>'))

    if cho == 1:
        hak = int(input('학번>'))
        score = int(input('점수>'))

        stu1 = Stu(hak,score)
        stulist.append(stu1)
        
    elif cho == 2:
        print("정렬 된 학번 리스트")
        pass
    elif cho == 3:
        # 순위표 출력 
        pass
    elif cho == 0:
        break



# 1002 20
# 1001 100
# 1005 60
# 1003 40
# 1004 50

# 1. 학번을 먼저 정리를 하기
# 2. 순위 100 -> 60 -> 50 -> 40 -> 20
#   1등 100  1001
#   2등 60   1005
#   3등 50   1004






    
