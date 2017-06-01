'''
Created on Jun 1, 2017

@author: xdussap
'''
from os.path import os


if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt")
    inputfile = open(path)

    row_col_count, blockers = list(map(int, inputfile.readline().strip().split(" ")))

    queen_row, queen_col = list(map(int, inputfile.readline().strip().split(" ")))
#     queen_row -= 1
#     queen_col -= 1

#     print(datetime.now())
#     matrix = [[True for _ in range(row_col_count)] for _ in range(row_col_count)]
#     print(datetime.now())
#     print(matrix)

    east_rows = 1
    west_rows = row_col_count
    north_columns = 1
    south_columns = row_col_count
    north_east_column = 1
    south_east_column = 1
    north_west_column = row_col_count
    south_west_column = row_col_count

    for _ in range(blockers):
        block_row, block_col = list(map(int, inputfile.readline().strip().split(" ")))
#         Check East
        if block_row < queen_row and block_col == queen_col:
            east_rows = block_row if east_rows < block_row else east_rows
#         Check West
        elif block_row > queen_row and block_col == queen_col:
            west_rows = block_row if west_rows > block_row else west_rows
#         Check North
        elif block_row == queen_row and block_col < queen_col:
            north_columns = block_col if north_columns < block_col else north_columns
#         Check South
        elif block_row == queen_row and block_col > queen_col:
            south_columns = block_col if south_columns > block_col else south_columns
#         check North East
        elif block_row < queen_row and block_col < queen_col:
            north_east_rows = block_row if north_east_rows < block_row else north_east_rows
#         Check South East
        elif block_row < queen_row and block_col > queen_col:
            south_east_rows = block_row if south_east_rows < block_row else south_east_rows
#         Check North West
        elif block_row < queen_row and block_col < queen_col:
            north_west_rows = block_row if north_west_rows > block_row else north_west_rows
#         Check South West
        elif block_row < queen_row and block_col < queen_col:
            south_west_rows = block_row if south_west_rows > block_row else south_west_rows

    
    icount = (queen_row - east_rows) + (west_rows - queen_row) + (queen_col - north_columns) + (south_columns - queen_col) + (queen_row - north_east_rows) + (queen_row - north_east_rows) + (north_west_rows - queen_row) + (south_west_rows - queen_row)
    print(icount)
    
    
