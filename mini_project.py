""""
식권 자판기 프로그램 만들기
1. 관리자 : 식권 충전, 잔돈 충전, 뒤로가기
2. 사용자 : 구입 입금액, 구매 매수 입력

"""
moneys = [50000, 10000, 5000, 1000, 500, 100] # 잔돈
charges = [1,1,1,1,5,10] # 잔돈 개수
tickets = 5 # 식권 개수
price = 3200 # 식권 가격

while True:
  print('[1] 관리자')
  print('[2] 사용자')

choice = int(input('>'))

if choice == 1:
  while True:
    print('식권 수량 : ', tickets)
    i = 0
    while i<len(moneys):
      print(moneys[i],':',charges[i])
      i+=1

    print('1) 식권 충전')
    print('2) 잔돈 충전')
    print('3) 뒤로 가기')

    sel = int(input('>'))
    if sel == 1:
      count = int(input("충전할 식권 수를 입력하세요: "))
      tickets += count
    elif sel == 2:
      while True:
        i = 0
        while i<len(moneys): # 잔액 조회
          print('[%d] %d : %d장'%(i+1, moneys[i], charges[i]))
          i+=1
          print('[0] 뒤로가기') # 위에 잔액을 조회하지 않을 경우에는 뒤로가기

          num = int(input('>'))
          if num == 0:
            break
          else:
            charges[num-1] += 1
            # num 메뉴는 0부터 입력 계산해라
    elif sel == 3:
      break
elif choice == 2:
  while True:
    print('1) 구입')
    print('2) 뒤로가기')

    sel = int(input('>'))

    if sel == 1:
      count = int(input('몇 개의 식권을 구입 :'))
      if count > tickets:
        continue
      result = count*price
      print('총 금액 :', result)

      my_charges = [0 for i in range(len(moneys))]

      print('돈을 넣어주세요')

      while True:
        i=0

        while i<len(moneys):
          print('[%d] %d: %d장'%(i+1, moneys[i], charges[i]))
          i+=1
        print('[0] 뒤로가기')
        num = int(input('>'))

        if num == 0:
          break
        else:
          my_charges[num-1]+=1
          my_result = 0
          i=0
          while i<len(my_charges):
            my_result = my_charges[i]*moneys[i]
            i+=1

          print(my_result,'원 입금했습니다')
          charge = my_result-result
          print('잔돈:', charge)
    elif sel == 2:
      break