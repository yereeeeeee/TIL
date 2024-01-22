# 아래 함수를 수정하시오.
def count_character(my_list, x):
    count = my_list.count(x)
    return count


result = count_character("Hello, World!", "o")
print(result)  # 2
