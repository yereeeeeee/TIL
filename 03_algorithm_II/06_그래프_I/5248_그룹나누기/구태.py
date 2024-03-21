import sys
sys.stdin = open('input.txt')

def recur(info, length):
    final = [info.pop(0)]

    for idx in range(len(info)):
        print(idx, final)
        for k in range(len(final)):
            if final[k] & info[idx]:
                final[k] = final[k] | info[idx]
                break
        else:
            final.append(info[idx])
    if length == len(final):
        return final
    return recur(final, len(final))


T = int(input())

for tc in range(1, T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))

    info = [{0} for _ in range(N+1)]
    # print(info)

    for i in range(N+1):
        info[i] = {i}

    # print(info)

    for j in range(M):
        info[arr[j*2]].add(arr[j*2+1])
        info[arr[2*j+1]].add(arr[2*j])

    info.pop(0)
    print(info)

    result = recur(info, len(info))
    print(len(result))