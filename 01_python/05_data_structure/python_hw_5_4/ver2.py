# 아래 함수를 수정하시오.
def find_min_max(arr):
    # 파이썬 함수의 특징
    # 파이썬 함수는 반드시 반환하는 값이 하나의 객체이다.
    # 그런데, 만약 2개 이상의 객체를 반환하도록 하려고 하면,
    # 파이썬이 알아서 tuple로 묶어서 반환한다.
    return min(arr), max(arr)

def find_max(arr):
    # 항상 arr 안에는 0 이상의 정수만 있다고 가정.
    # arr에 들어 있는 값보다 무조건 제일 작은 값이
    # 초기 비교 대상 값이 되어야 한다.
    # 그러므로 result는 0으로 초기화 한다.
    result = 0
    # 비교한다? -> 결국 전체 배열 모두 순회
    for num in arr:
        # 만약 배열이 가진 요소가 result보다 크다면?
        # 최댓값을 찾는 중이니, result의 값을 num으로 바꾼다.
        if result < num:
            result = num
    return result

def find_min(arr):
    # 최솟값인 경우, 초기값 설정: 충분히 큰 수
    # 우리의 비교 대상 -> arr
    # 그럼 범위는 사실, 항상 arra이 가진 모든 요소를 벗어나지 않음
    result = 9999
    for num in arr:
        if result > num:
            result = num
    return result


result = find_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)