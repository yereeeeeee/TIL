############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_position_safe(N, M, current):
    # 여기에 코드를 작성하여 함수를 완성합니다.

    # 최대 범위 (a, b)
    a = range(N)
    b = range(N)

    # 현재 위치를 리스트로 반환
    ls = list(current)
    x = 0
    y = 0

    # 움직인 위치를 x, y로 받아옴.
    if M == 0: x = ls[0] - 1
    elif M == 1: x = ls[0] + 1
    elif M == 2: y = ls[1] - 1
    else: y = ls[1] + 1

    # 범위 내에 있지 않을 경우 False, 그렇지 않으면 True를 반환
    if x in a and y in b:
        return True
    else: return False
    

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(is_position_safe(3, 1, (0, 0))) # True
print(is_position_safe(3, 0, (0, 0))) # False
#####################################################
