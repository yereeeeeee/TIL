n = int(input())
result = 0
for i in range(n):
    char = list(input())
    char_ls = []

    # 길이가 1이면 그룹 단어
    if len(char) == 1:
        result += 1
        break

    while char:
        c = char.pop(0)
        if (c not in char_ls) or (c == char_ls[-1]):
            char_ls.append(c)
        else:
            break
    else:
        result += 1
print(result)