oh = 0
ov = 0

for row in range(5):
    r = list(map(int, input().split(" ")))
    for col in range(5):
        if r[col]==1:
            if row<2:
                oh = 2-row
            elif row>2:
                oh = row-2

        if r[col]==1:
            if col<2: 
                ov = 2-col
            elif col>2:
                ov = col-2

move = oh+ov
print(move)
