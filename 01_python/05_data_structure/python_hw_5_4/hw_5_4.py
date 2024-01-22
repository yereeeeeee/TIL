# 아래 함수를 수정하시오.
def find_min_max(num_list):
    num_list.sort()
    return (num_list[0], num_list[-1])


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
