def heapify_up(heap, index):
    while index > 0:    # index가 0이면 루트 노드임
        parent_index = (index - 1) // 2 # 완전 이진트리의 부모 노드는 자식 노드의 index // 2
        if heap[parent_index] > heap[index]:    # 루트 노드가 아닐 때 부모 노드가 더 크면
            heap[parent_index], heap[index] = heap[index], heap[parent_index]   # 부모와 자식을 바꿔줌
            index = parent_index
        else:
            break


def min_heap_sum(N, nums):
    heap = []  # 최소힙을 구현하기 위한 리스트

    # 최소힙에 자연수들을 저장
    # 힙에 수를 하나하나 넣는데,
    # 넣고 나서 heapify_up() 함수를 통해 최소힙인지 확인해줌.
    for num in nums:
        heap.append(num)
        heapify_up(heap, len(heap) - 1)

    # 마지막 노드의 조상 노드에 저장된 정수의 합 계산
    sum_ancestors = 0
    # idx를 아래와같이 정한 이유는 현재까지 생성된 heap 리스트에 가장 마지막에 새로운 요소를 넣어줘야 하기 때문
    # 힙 생성 방법임
    index = len(heap) - 1

    while index > 0:        # 루트 노드까지
        parent_index = (index - 1) // 2     # 조상 노드에 적힌 값을 다 더해줌
        sum_ancestors += heap[parent_index]
        index = parent_index

    return sum_ancestors


# 테스트 케이스 수 입력
T = int(input())

# 각 테스트 케이스 실행
for test_case in range(1, T + 1):
    # 자연수의 개수 N 입력
    N = int(input())
    # 자연수들 입력
    nums = list(map(int, input().split()))

    # 최소힙에 저장된 조상 노드들의 합 계산
    result = min_heap_sum(N, nums)

    # 결과 출력
    print(f"#{test_case} {result}")