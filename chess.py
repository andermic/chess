import re

def square_to_indexes(sq):
    return (8 - (int(sq[1])), ord(sq[0]) - ord('a'))


def is_game_over():
    return False #TODO


def reset_board():
    global board
    board[0] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
    board[1] = ['p'] * 8
    board[2] = board[3] = board[4] = board[5] = [' '] * 8
    board[6] = ['P'] * 8
    board[7] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']


def display(message = ''):
    top_left      = '\u2554'
    top_right     = '\u2557'
    bot_left      = '\u255A'
    bot_right     = '\u255D'
    
    top_edge      = '\u2566'
    bot_edge      = '\u2569'
    left_edge     = '\u2560'
    right_edge    = '\u2563'
    
    hori_line     = '\u2550'
    vert_line     = '\u2551'
    intersection  = '\u256C'
    
    hori_lines = hori_line * 3
    
    top_border_line = top_left  + (hori_lines + top_edge)*7     + hori_lines + top_right
    mid_border_line = left_edge + (hori_lines + intersection)*7 + hori_lines + right_edge
    bot_border_line = bot_left  + (hori_lines + bot_edge)*7     + hori_lines + bot_right
    
    print(message)
    for i in range(8):
        print(top_border_line if i == 0 else mid_border_line)
        print(vert_line + ' ' + (' ' + vert_line + ' ').join(board[i]) + ' ' + vert_line)
    print(bot_border_line + '\n')


def try_move(move):
    ### Parse move command ###
    
    ranks = '[12345678]'
    files = '[abcdefgh]'
    pieces = '[rnbqkp]'
    
    piece = None
    start_square = None
    end_square = None
    promote_to = None
    
    #Moves like "e4"
    if re.match(files+ranks+'$', move) != None:
        piece = 'p'
        end_square = move
    
    #Moves like "Bg5"
    elif re.match(pieces+'x?'+files+ranks+'$', move) != None:
        piece = move[0]
        end_square = move[-2:]
    
    #Moves like "e2e4"
    elif re.match(files+ranks+'x?'+files+ranks+'$', move) != None:
        start_square = move[:2]
        end_square = move[-2:]
    
    #Moves like "Rbd6"
    elif re.match(pieces+files+'x?'+files+ranks+'$', move) != None:
        piece = move[0]
        start_square = move[1] + move[-1]
        end_square = move[-2:]

    #Moves like "R8d6"
    elif re.match(pieces+ranks+'x?'+files+ranks+'$', move) != None:
        piece = move[0]
        end_square = move[-2:]

    #Moves like "exd5"
    elif re.match(files+'x?'+files+ranks+'$'):
        piece = 'p'
        start_square = 
    
    #Moves like "0-0"
    elif re.match('0-0(-0)?$'):
        piece = 'k'
        rank = '1' if player_turn else '8'
        start_square = 'e' + rank
        end_square = 'g' if len(move) == 3 else 'c' + rank
    
    #Moves like "e8=Q"
    elif re.match('p?'+files+'[18]=[bnrq]$', move) != None:
        piece = 'p'
        start_square = move[0] + '2' if move[1] == '1' else '7' #TODO:FIX
        end_square = move[:2]
        promote_to = move[3]

    #Moves like "dxe8=Q"
    
    else:
        print('Invalid move')  #TODO: Fix, user probably won't see this
        return

    print('piece, start square, end square, promote to')
    print(piece, start_square, end_square, promote_to)

    start_indexes = square_to_indexes(start_square)
    end_indexes = square_to_indexes(end_square)

    #TODO: Retest above. Be thorough or there will be bug(s).

    ### Make move if it's valid ###
    
    #TODO Make move
    ##Check if an appropriate piece of the appropriate color can be moved from the start square to the end square
    ###Ambiguous moves are invalid
    ##Handle castling, en passant, and promotion
    ##Update the board
    ##Track last move for en passant

def is_game_over():
    pass
    

board = [[' '] * 8] * 8
reset_board()

display()

#Game loop
player_turn = True
can_castle_w = True
can_castle_b = True
while not is_game_over():
    command = input('>').lower()
    display(try_move(command))
    
