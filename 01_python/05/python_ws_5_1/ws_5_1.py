# 아래 함수를 수정하시오.
def reverse_string(string):
    st_list = reversed(string)
    for char in st_list:
        print(char, end='')
    


result = reverse_string("Hello, World!")
#print(result)  # !dlroW ,olleH
