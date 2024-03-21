def check_(sudoku):
    if 0 in sudoku:
        return False

    # 가로
    for i in sudoku:
        cnt = [0] * 9
        for j in i:
            if cnt[j-1] == 0:
                cnt[j-1] = 1
            else:
                return False
        if 0 in cnt:
            return False

    # 세로
    for i in range(9):
        cnt = [0] * 9
        for j in range(9):
            if cnt[sudoku[j][i]-1] == 0:
                cnt[sudoku[j][i]-1] = 1
            else:
                return False
        if 0 in cnt:
            return False

    # 3x3
    for i in range(3):
        for j in range(3):
            cnt = [0] * 9
            for a in range(3):
                for b in range(3):
                    if cnt[sudoku[i*3+a][j*3+b]-1] == 0:
                        cnt[sudoku[i*3+a][j*3+b]-1] = 1
                    else:
                        return False
            if 0 in cnt:
                return False

def input_sudoku(sudoku):
    pass

arr = [list(map(int, input())) for _ in range(9)]
