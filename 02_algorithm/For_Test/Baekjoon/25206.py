grade = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}
result = 0.0
cnt = 0
while 1:
    try:
        sub, crd, grd = list(map(str, input().split()))
        crd = float(crd)
        if grd == 'P':
            pass
        else:
            result += crd*grade[grd]
            cnt+=crd
    except:
        break

print(result / cnt)
