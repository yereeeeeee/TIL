data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.
for dt in data:
    for key in key_list:
        if dt.get(key) == None:
            dt.setdefault(key, 'unknown')
            print(f'{key}은/는 {dt.get(key)}입니다.')
        else:
            print(f'{key}은/는 {dt.get(key)}입니다.')
    print()