# 아래 함수를 수정하시오.
def even_elements(ls):
    for i in range(len(ls)):
        if ls[i] % 2 == 0:
            print(ls[i])
            item = ls.pop(i)
            new_list = []
            new_list.append(item)
    return new_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)