# 아래 함수를 수정하시오.
def even_elements(ls):
    even = []
    even2 = []
    while ls:
        ab = ls.pop(0)
        if ab % 2 == 0:
            even.append(ab)
    even2.extend(even)
    return even2 

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)