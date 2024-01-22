data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.
new_1 = []
for char in data_1:
    if char.isupper() == True or char == ' ':
        new_1.append(char)
print(''.join(new_1))

data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.
for char in '내힘들다':
    arr.append(data_2.index(char))
print(arr)

arr.sort()
print(arr)

new_2 = []
for a in arr:
    new_2.append(data_2[a])
print(''.join(new_2))