""""
이진탐색(이분탐색)
무조건 오름차순이던 내림차순이던 정렬이 먼저 되어있어야한다.
검색 - 정렬된 상태에서 빠르게 원하는 것을 찾을 수 있음.
기준점을 잡아서 비교를 한 다음에 데이터가 작으면 앞 쪽 검색
기준점보다 크면 뒷쪽 검색

순차탐색은 앞에서부터 차례대로 찾는 것이므로
정렬X

트리 검색 
- 데이터 검색에는 상당히 효율적으로 트리의 삽입, 삭제
"""
list = [7,3,6,2,1,3,8]
#num = int(input())


#함수 없이 구현
#start = 0 # 시작점
#end = len(list)-1 # 끝지점

#데이터가 있는지 없는지 구별
#check = -1 # 대부분 데이터가 없음을 의미
            # 만약 데이터가 있다 - > 인덱스를 저장

    # while start <= end:
    #     mid = (start+end) // 2
    #     if num == list[mid]:
    #         print(mid,"번째 방에 있다")
    #         break
    #     elif num<list[mid]:
    #         end = mid-1
    #     else:
    #         start = mid+1
    # if check != -1:
    #     print(check, "번째 방에 있다.")
    # else:

#함수로 구현

def binary_search(find_list, key):
    start = 0
    end = len(find_list)-1
    while start <= end:
        mid = (start+end) // 2
        if key == list[mid]:
            print(mid,"번째 방에 있다")
            return mid
        elif key<list[mid]:
            end = mid-1
        else:
            start = mid+1
    return -1

result = binary_search(list, 1)
print(result)
result = binary_search(list, 10)
