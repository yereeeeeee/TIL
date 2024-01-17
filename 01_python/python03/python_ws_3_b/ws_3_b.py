pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

def create_data(subject = None, day = None, title = None):
    data = {}
    data['subject'] = subject
    data['day'] = day
    data['title'] = title
    data['문제 번호'] = pro_num + 1
    return data


result_1 = create_data()
result_2 = create_data()
result_3 = create_data()
