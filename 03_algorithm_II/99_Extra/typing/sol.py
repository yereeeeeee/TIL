import sys
sys.stdin = open('input.txt', encoding='UTF-8')
from itertools import permutations

N = int(input())
S, P = map(int, input().split())    # 강사님 점수
teacher = int(S*P/100)
# print(int(S*P/100), '강사님')
scores = []
# 팀번호 : [학생1점수, 학생1정확도, 학생1언어구분, 학생1이름],
#         [학생2점수, 학생2정확도, 학생2언어구분, 학생2이름]

num_list = list(permutations([0, 1, 2], 3))
# print(num_list)

def cal(score):
    score = list(score)
    tmp = float('inf')

    for i in range(len(num_list)):
        result = ''
        for j in range(3):
            result += str(score[num_list[i][j]])
        if abs(int(result)-teacher) < tmp:
            tmp = abs(int(result)-teacher)
    return tmp

for i in range(1, N+1):
    team = []
    for j in range(2):
        student = list(input().split())
        score = float(student[0]) * (float(student[1])/100)
        if student[2] == 'K':
            score *= 0.7
        team.append(((int(score), student[3], i)))

    # print(team)
    team_score = (team[0][0] + team[1][0]) // 2
    # print(cal(str(team_score)))
    scores.append([cal(str(team_score)), [team[0][1], team[1][1]], team[0][2], team_score])

scores.sort(key=lambda x:(x[0], -x[3]))
print(scores)
for j in range(1, N+1):
    print(f'{j}등 : {scores[j-1][1][0]} {scores[j-1][1][1]} ({scores[j-1][2]} 팀) | 점수 차: {scores[j-1][0]} | 원점수 : {scores[j-1][3]}')
