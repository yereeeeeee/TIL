one = 3
two = 5

print(one or two) # 3 : 단축 평가 (two까지 진행 x)

if one or two: # if 3:
    print('and 연산 통과')
else:
    print('and 연산 통과 못함')

print(0 == False) # True
print(-1 == False) # False
print('' == True) # False
print('' == False) # False

if '':
    print('빈 문자열 == 빈 문자열?')
else:
    print('아무일도 벌어지지 않음')

three = ''
four = '4'
print(three and four)
if three and four:
    print('3과 4')
else:
    print('실패')


if one % 2 == 1:
    print('홀수')
else:
    print('짝수')

if one % 2:
    print('홀수')