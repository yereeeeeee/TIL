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
    #'난중일기'
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

'''
대여 예정 도서 리스트 중 보유하지 않은 책이 있는가?
보유 하지 않은 책이 있다면 문구 출력
모든 책을 보유 중이라면 다른 문구 출력
'''

have_all_book = True


for rental in rental_list:
    have_book = False
    
    for books in list_of_book:       

        if rental == books:
            have_book = True

    if have_book == False:
        have_all_book = False
        print(f'{rental}은/는 보유하고 있지 않습니다.')
        break


if have_all_book == True:
    print('모든 도서가 대여 가능한 상태입니다.')