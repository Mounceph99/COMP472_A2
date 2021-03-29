# Requirements
To run this project, make sure that `Python 3.8` and `jupyter` are installed. 


# Running the project
To run the project, start a Jupyter Notebook instance (run `jupyter notebook` in a terminal from this directory) and open the Notebook in this project.

In the first cell of the notebook, program parameters can be set:

- `TIME_LIMIT` is the max execution time of a solver/algorithm (in seconds). Set to -1 for unlimited execution time.

- `PUZZLES_FILE` is the input file containing S-Puzzles that the program will solve (using DFS, I-D, and A*). The format of the file can be very flexible.
The only requirements are that puzzles must be on their own line, and that the numbers of the puzzles must be in order (left to right, top to bottom) and separated (by at least 1 non-numerical character).
For example, the program would succesfully parse the following 4 puzzles:

```
((6; 1; 2); (7; 8; 3); (5; 4; 9))
5, 1, 3, 4, 9, 6, 7, 2, 8
((9, 4, 6), (7, 2, 1), (3, 5, 8))
2, 3, 7 / 8, 6, 5 / 9, 1, 4
```

- OUTPUT_DIR is the directory where results and statistics files will be outputted to.

From there, `Cell > Run All` will run all the cells. After a succesful execution of the project, files will be created in OUTPUT_DIR.
In particular, two files will be created per solver/algorithm: their solution paths (if found), and their search paths (if a solution was found).
Additionally, a `statistics.txt` file will also be outputted, containing relevant information to compare the solvers/algorithms executed on the input puzzles.

# Team Members
Team \#13

Luc Nguyen (40097582)

Chelsea Guan (40097861)

Joseph Loiselle (40095345)

Mounceph Morssaoui (40097557)