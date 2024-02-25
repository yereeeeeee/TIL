string = input()
n = len(string)
i = 0
while i < n:
    if string[i] == string[n-i-1]:
        i += 1
    else:
        print(0)
        break
else:
    print(1)