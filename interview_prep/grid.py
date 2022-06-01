num_rows = 2
num_columns = 3 
grid = []

for _ in range(num_rows):
    curr_row = []
    for _ in range(num_columns):
        curr_row.append(0)
    grid.append(curr_row)

print(grid)

grid2 = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
print(grid2)