num_puzzles = 20
output_file = 'random_puzzles.txt'
size = 3 # 3 for 3x3, 4 for 4x4, etc.

from random import shuffle

if __name__ == '__main__':
    state = [ (i+1) for i in range(size*size) ]
    with open(output_file, 'w') as f:
        for i in range(num_puzzles):
            shuffle(state)
            puzzle_state = tuple( tuple(state[i:(i+size)]) for i in range(0, size*size, size) )
            f.write(str(puzzle_state))
            f.write('\n')