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

