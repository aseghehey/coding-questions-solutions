board = ['XOX', 'OXO','.X.']

n = len(board)
# for i in range(len(board)):
#     count_x, count_o = 0,0
#     for j in range(len(board[i])):
#         if board[i][j] == '.':
#             break
#         if board[i][j] == 'X':
#             count_x += 1
#         if board[i][j] == 'O':
#             count_o += 1
        
#     if count_x == n:
#         print('X WON')
#         break

#     if count_o == n:
#         print('O WON')
#         break

# j = 0
countX = 0
countO = 0
for i in range(len(board)):
    print(board[i][i])
    if board[i][i] == 'X':
        countX += 1
    if board[i][i] == 'O':
        countO += 1

print()
j = 0
for i in range(len(board) - 1, -1, -1):
    print(board[i][j])
    if board[i][i] == 'X':
        countX += 1
    if board[i][j] == 'O':
        countO += 1
    j += 1

# print(board)
# print(board[::-1])
