# sorting-numbers-using-various-search-algorithms

# Sorting as Searching Problem


## Description

This project explores and analyzes various searching algorithms applied to a set of numbers with the objective of arranging the given set of numbers in ascending order using different search algorithms.

For each algorithm, experiments were conducted using Python code. The input to the code consists of a number 'n' followed by 'n' numbers. The final output includes:

- The path taken from the start state to the goal state (in case of uninformed and informed search methods).
- The final state (in case of local hill-climbing search).
- The total number of nodes explored during the search process for analysis.

In the context of informed search algorithms, the heuristic function employed evaluates the number of numbers that are not in their correct positions within a node relative to the desired goal state.


## Usage

To run the code, follow these steps:

1. Execute the Python script: `python file.py`

2. Enter a number 'n' to indicate the number of numbers.

3. Input 'n' numbers as required.

The code will output the following:

- The path to the goal state (sorted state) and the number of nodes explored for uninformed and informed search methods.
- The final state (which might be suboptimal) and the number of nodes explored for local hill-climbing search.


## Sample Inputs

I have provided a set of sample inputs (which were used during analysis) in the `inputs.txt` file. Each line in the file represents an input test case, consisting of a number 'n' followed by 'n' numbers.

### How to Use the Sample Inputs

1. Open the `inputs.txt` file in a text editor or your preferred code editor.

2. Choose a test case by selecting a line from the file.

3. Copy the selected test case and paste it into the input prompt when running the Python code.

4. Run the code, and it will process the selected test case and provide the output.


## Acknowledgements

- Hacettepe University, Department of Computer Science.
- VBM688: Introduction to Artificial Intelligence.
- Pseudo-codes used in the project were adapted from [VBM688 Course Material](https://web.cs.hacettepe.edu.tr/~ilyas/Courses/VBM688/).
