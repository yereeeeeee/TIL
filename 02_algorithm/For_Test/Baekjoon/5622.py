ls = [[], [], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
a = list(input())
result = 0
for i in a:
    for j in ls:
        if i in j:
            result += ls.index(j) + 1
print(result)