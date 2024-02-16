N = int(input())
balloons = list(map(int, input().split()))

here = 0
visited = [0]

def b_pop():


while len(visited) < N:
    next_ = balloons[here] % N
    if here+next_ not in visited:
        here += next_
        visited.append(here)
        if here+next_ > 0:
            here = balloons[(here+next_)%N]
        else:
            here = balloons[here+next_+N]
    else:
        if here < 0:
            for i in range(5, -1, -1):
                if i not in visited:
                    here = i
                    visited.append(here)
                    here = balloons[here + next_]
                    break
        else:
            for i in range(0, 5):
                if i not in visited:
                    here = i
                    visited.append(here)
                    here = balloons[here + next_]
                    break
print(visited)




