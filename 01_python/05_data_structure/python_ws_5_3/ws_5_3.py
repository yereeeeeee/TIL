# 아래 함수를 수정하시오.
def sort_tuple(tp):
    new_tuple = ()
    ls = list(tp)
    ls.sort()
    new_tuple = tuple(ls)
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
