"""
공백 없애는 함수 2가지
1. strip() : 중간에 있는 공백 못 없앰;
2. replace(변경 전 문자, 변경 후 문자 )
문자열.replace(" ","")
for문으로 공백 없앨 수 있음.
for c in str1:
    if c != '.' and c != ' ':
        str2 = str2+c     # 파이썬에서 문자는 더하기 가능(연결)
"""
input_string = input()
string = input_string.replace(" ","")
print(input_string)
print(string)

is_pali = True

for i in range(len(string)//2):
  if string[0] != string[-1 - i]: # 왼쪽 문자랑 오른쪽에 있는 문자가 다르면
    is_pali = False
    break
#string[-1 - i] : i가 첫번째면 -1-i는 마지막