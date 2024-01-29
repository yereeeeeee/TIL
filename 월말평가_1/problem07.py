############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count()를 사용하지 않습니다.
def tidy_up_company(email_list):
    # 여기에 코드를 작성하여 함수를 완성합니다.

    # 중복이 없는 e set를 활용하여 비교 예정
    e_set = set(email_list)

    # d = 반환될 dict, e set에 있는 인자를 key값으로 가짐
    d = {}
    for i in e_set:
        d[i]=0
    
    # 리스트에 있는 요소와 비교하여 해당 key에 대한 value를 1씩 올려줌
    for e in email_list:
        d[e] += 1

    return d

    



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
email_list1 = ['Koogle', 'Koogle', 'Maver']
print(tidy_up_company(email_list1))   # {'Koogle': 2, 'Maver': 1}

email_list2 = [
    'Koogle', 'Koogle', 'JCloud', 'Koogle', 'GaKao', 
    'School', 'Koogle', 'Maver', 'GaKao', 'Maver', 
    'Koogle', 'GaKao', 'School', 'GaKao', 'JCloud', 
    'School', 'GaKao', 'GaKao', 'Maver', 'Koogle'
]
print(tidy_up_company(email_list2))
# {'Koogle': 6, 'JCloud': 2, 'GaKao': 6, 'School': 3, 'Maver': 3}
#####################################################
