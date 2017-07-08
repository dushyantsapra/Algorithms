'''
Created on Jun 1, 2017

@author: xdussap
'''


if __name__ == '__main__':
    inputfile = open("/home/sapra/input.txt");

    row_col_count, blockers = list(map(int, inputfile.readline().strip().split(" ")))

    queen_row, queen_col = list(map(int, inputfile.readline().strip().split(" ")))

    east_rows = queen_row - 1
    west_rows = row_col_count - queen_row
    north_columns = queen_col - 1
    south_columns = row_col_count - queen_col
    
    north_east_column = min(queen_row - 1, queen_col - 1)
    south_east_column = min(queen_row - 1, row_col_count - queen_col)
    north_west_column = min(row_col_count - queen_row, queen_col - 1)
    south_west_column = min(row_col_count - queen_row, row_col_count - queen_col)
    
    blockers_map = {}
    for _ in range(blockers):
        block_row, block_col = list(map(int, inputfile.readline().strip().split(" ")))
        blockers_map[(block_row, block_col)] = True
#         Check East
        if block_row < queen_row and block_col == queen_col:
            if block_row < queen_row and queen_row - block_row - 1 < east_rows:
                east_rows = queen_row - block_row - 1
#         Check West
        elif block_row > queen_row and block_col == queen_col:
            if block_row > queen_row and block_row - queen_row - 1 < west_rows:
                west_rows = block_row - queen_row - 1
#         Check North
        elif block_row == queen_row and block_col < queen_col:
            if queen_col > block_col and queen_col - block_col - 1 < north_columns:
                north_columns = queen_col - block_col - 1
#         Check South
        elif block_row == queen_row and block_col > queen_col:
            if queen_col < block_col and block_col - queen_col- 1 < south_columns:
                south_columns = block_col - queen_col- 1
#         check North East
        elif block_row < queen_row and block_col < queen_col:
            if queen_col > block_col and queen_col - block_col - 1 < north_east_column:
                north_east_column = queen_col - block_col - 1
#         Check South East
        elif block_row < queen_row and block_col > queen_col:
            if queen_col < block_col and block_col - queen_col - 1 < south_east_column:
                south_east_column = block_col - queen_col - 1
#         Check North West
        elif block_row > queen_row and block_col < queen_col:
            if queen_col > block_col and queen_col - block_col - 1 < north_west_column:
                north_west_column = queen_col - block_col - 1
#         Check South West
        elif block_row > queen_row and block_col > queen_col:
            if queen_col < block_col and block_col - queen_col - 1 < south_west_column:
                south_west_column = block_col - queen_col - 1

#     delete_count = 0
#     if (east_rows, queen_col) in blockers_map:
#         delete_count += 1
#     if (west_rows, queen_col) in blockers_map:
#         delete_count += 1
#     if (queen_row, north_columns) in blockers_map:
#         delete_count += 1
#     if (queen_row, south_columns) in blockers_map:
#         delete_count += 1
#     if (queen_row - (queen_col - north_east_column), north_east_column) in blockers_map:
#         delete_count += 1
#     if (queen_row - (south_east_column - queen_col), south_east_column) in blockers_map:
#         delete_count += 1
#     if (queen_row + (queen_col - north_west_column), north_west_column) in blockers_map:
#         delete_count += 1
#     if (queen_row + (south_west_column - queen_col), south_west_column) in blockers_map:
#         delete_count += 1
    

    icount = (east_rows) + (west_rows) + (north_columns) + (south_columns) + (north_east_column) + (south_east_column) + (north_west_column) + (south_west_column)
#     print(icount)
    print(icount)
    
    
