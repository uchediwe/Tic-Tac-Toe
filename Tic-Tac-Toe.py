n = 3
mat = [['.'] * n for i in range(n)]

# Main function: alternately prompt the two human
# players - 'X' and 'O' - by calling get_move function.
#
def main():
    num_moves = 0
    print_mat()
    print('Moves are r, c or "0" to exit.')
    exit_flag = False
    while not exit_flag:
        num_moves += 1
        if num_moves > 9:
            print('No more space left.')
            break
        player_ch = 'X' if num_moves % 2 > 0 else 'O'
        exit_flag, r,c = get_move(player_ch)

# Get Move function.
# Prompt and re-prompt human player ('X' or 'O')
# until a valid move of form 'row, col' has been
# entered at an available square.  Then enter move
# into the grid and re-print the gid display.
def get_move(player_ch):
    while True:
        prompt = 'Enter move for ' + player_ch + ': '
        s = input(prompt)
        a_list = s.split(',')
        if len(a_list) >= 1 and int(a_list[0])==0:
            print('By now.')
            return  True, 0,0 # Throw 'EXIT' flag
        elif len(a_list)<2:
            print('Use row, col. Re-enter.')
        else:
            # First, convert to 0-based indexes.
            r = int(a_list[0])-1
            c = int(a_list[1])-1
            if r<0 or r>=n or c<0 or c>=n:
                print('Out of range. Re-enter.')
            else:
                mat[r][c] = player_ch
                print_mat()
                break
    return False, r, c # Do not throw 'EXIT' flag

def print_mat():
    s = ' 1 2 3\n'
    for i in range(n):
        s += str(i+1)+' '
        for j in range(n):
            s+= str(mat[i][j]) + ' '
        s += '\n'
    print(s)

main()