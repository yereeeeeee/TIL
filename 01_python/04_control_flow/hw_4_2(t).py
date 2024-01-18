list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_list = [
    '장생전',
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]

check = False
# rental_list에 있는 요소 중, 하나라도 list_of_book
# 없는 책이 있 으면 반복문 종료

for rental in rental_list:
    # 전체 책 목록중
    # 대여 대상과 비교할 때, 같은 이름이 있는지 체크용
    book_found = False
    for book in list_of_book:
        #print(book, rental)
        if book == rental:
            book_found = True
            break 
    # 전체 책 목록을 모두 순회했으나, 같은 책을 발견하지 못함.
    if book_found == False:
        check = False
        print(f'{rental} 책은 보유하고 있지 않음')
        break
if check == True:
    print('모든 책이 다있음.')


# 반대로 생각해보기
for rental in rental_list:
    # 대여하려는 책이 목록에 없으면
    if rental not in list_of_book:
        print(f'{rental} 책은 없음')
        break
if check == True:
    print('책 다 있음.')


# 반복문은 break로 강제 종료된 것과 아닌 것 구분
for rental in rental_list:
    if rental not in list_of_book:
        print(f'{rental} 책은 없음')
    # break 문은 현재 실행중인 반복문을 종료
    # 중첩 반복문인 경우엔, 모든 반복문 종료는 아니다.
        break
# for ~ else 문은 break로 종료되지 않았다면 실행77
else:
    print('책 다 있음.')
