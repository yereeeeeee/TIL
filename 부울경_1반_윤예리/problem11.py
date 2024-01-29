############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def get_final_position(N, matrix, move_list):
    # 여기에 코드를 작성하여 함수를 완성합니다.

    # 최대 범위 (a, b)
    a = range(N)
    b = range(N)

    # 캐릭터의 현제 위치 구하기
    for i in matrix:
        if sum(i) == 1:
            x = matrix.index(i)
            for j in i:
                if j == 1:
                    y = i.index(j)
    
    # 캐릭터가 이동한 위치
    ls = [x, y]

    # move list에 맞게 이동한 위치
    # 단, 한번이라도 벗어나면 None을 출력함.
    for M in move_list:
        if x in a and y in b:
            if M == 0: x -= 1
            elif M == 1: x += 1
            elif M == 2: y -= 1
            else: y += 1
        else: return None

    return [x, y]
    
    



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
N = 3
matrix = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
] 
moves1 = [1, 1, 3]
print(get_final_position(N, matrix, moves1)) # [2, 1]

moves2 = [1, 2, 3, 3]
print(get_final_position(N, matrix, moves2)) # None
#####################################################
