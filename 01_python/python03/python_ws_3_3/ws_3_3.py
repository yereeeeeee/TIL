name = '홍길동'
number = 3

def rental_book():
    decrease_book()
    return print(f'{name}님이 {number}권의 책을 대여하였습니다.')
    
number_of_book = 100

def decrease_book():
    global number_of_book
    global number
    number_of_book = number_of_book - number
    return print(f'남은 책의 수 : {number_of_book}')

rental_book()