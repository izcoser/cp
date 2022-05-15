# B - Error Correction

while True:
    matrix = []
    size = int(input())
    if size == 0:
        break
        
    for i in range(size):
        row = [int(i) for i in input().split()]
        matrix.append(row)

    row_sums = [sum(r) for r in matrix]
    cols = [[r[i] for r in matrix] for i in range(size)]
    col_sums = [sum(col) for col in cols]

    bad_rows = [idx for idx, s in enumerate(row_sums) if s % 2 != 0]
    bad_cols = [idx for idx, s in enumerate(col_sums) if s % 2 != 0]

    if len(bad_rows) + len(bad_cols) == 0:
        print('OK')
    elif len(bad_rows) == 1 and len(bad_cols) == 1:
        print('Change bit (' + str(bad_rows[0] + 1) + ',' + str(bad_cols[0] + 1) + ')')
    else:
        print('Corrupt')