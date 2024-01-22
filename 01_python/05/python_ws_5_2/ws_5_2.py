# 아래 함수를 수정하시오.
def remove_duplicates(my_list):
    new_lst = []
    for i in my_list:
        num = my_list.count(i)
        new_lst.append(i)
        if num == 1:
            continue
        else:
            new_lst.remove()
            pass



    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
