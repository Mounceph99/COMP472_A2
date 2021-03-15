# for test purposes to compare two solvers
iterations = 100
size = 3 # 3 for 3x3, 4 for 4x4, etc.
solver1 = A_Star_Solver(heuristic=h2)
solver2 = A_Star_Solver(heuristic=h4)

# do not touch below
from random import shuffle

total_exec_time_solver1 = 0
total_exec_time_solver2 = 0

total_time_diff_solver1 = 0
total_time_diff_solver2 = 0

total_cost_diff_solver1 = 0
total_cost_diff_solver2 = 0

state = [ (i+1) for i in range(size*size) ]

for i in range(iterations):
    
    shuffle(state)
    puzzle_state = tuple( tuple(state[i:(i+size)]) for i in range(0, size*size, size) )

    puzzle_solver1 = S_Puzzle( puzzle_state )
    puzzle_solver2 = S_Puzzle( puzzle_state )

    _, solution_solver1, _, execution_time_solver1 = solver1.solve(puzzle_solver1)
    cost_solver1 = len(solution_solver1)-1
    
    _, solution_solver2, _, execution_time_solver2 = solver2.solve(puzzle_solver2)
    cost_solver2 = len(solution_solver2)-1
    
    total_exec_time_solver1 += execution_time_solver1
    total_exec_time_solver2 += execution_time_solver2
    
    total_time_diff_solver1 += execution_time_solver1-execution_time_solver2
    total_time_diff_solver2 += execution_time_solver2-execution_time_solver1
    
    total_cost_diff_solver1 += cost_solver1-cost_solver2
    total_cost_diff_solver2 += cost_solver2-cost_solver1

    print("====================================")
    print("iteration", i)
    display_puzzle_state(puzzle_state)
    print('Solver1 cost:', cost_solver1, ', Solver1 time:', execution_time_solver1, 's')
    print('Solver2 cost:', cost_solver2, ', Solver2 time:', execution_time_solver2, 's')

print()
print("===============================================================================================")
print('Average solver1 execution time', total_exec_time_solver1/iterations)
print('Average solver2 execution time', total_exec_time_solver2/iterations)
print()
print('Average solver1 time difference', total_time_diff_solver1/iterations)
print('Average solver2 time difference', total_time_diff_solver2/iterations)
print()
print('Average solver1 cost difference', total_cost_diff_solver1/iterations)
print('Average solver2 cost difference', total_cost_diff_solver2/iterations)