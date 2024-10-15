# 2048 Solver

This script implements a solution for a [2048 game simulation problem from Kattis](https://open.kattis.com/problems/2048).

## Problem Description

The solution takes a 4x4 grid of numbers and performs a move in one of four directions (left, up, right, down), according to the 2048 game rules. After combining the numbers, it prints the updated grid.

## Approach

- We represent the grid as a 1D list called `deck`.
- A helper function `add` combines tiles in the required direction.
- The solution handles four types of moves: left, up, right, and down using the Python `match-case` construct.

## Code Explanation

```python
# Insert snippets of code, like the `add` function
# 2048 Solver

This script implements a solution for the [2048 game problem on Kattis](https://open.kattis.com/problems/2048). The solution handles the movement and merging of tiles in the classic 2048 game based on the given move direction (left, up, right, or down).

## Problem Description

The program takes a 4x4 grid of numbers and a move direction as input. The grid simulates the state of a 2048 game, and the move direction specifies how the tiles should shift. The program outputs the updated grid after the move and combines the tiles according to the rules of 2048.

## Approach

1. The grid is stored as a 1D list named `deck`, where the 4x4 grid is flattened.
2. The `add` function merges adjacent tiles with the same value, shifting tiles to fill any empty spaces.
3. Based on the move direction (0: left, 1: up, 2: right, 3: down), the grid is processed, and the result is printed.

### Input Format:
1. The first four lines of input contain the 4x4 grid of integers.
2. The fifth line contains a single integer (0, 1, 2, or 3) representing the direction of the move.

### Output Format:
1. The updated 4x4 grid after performing the specified move.

## Code Explanation

The core functionality lies in the `add` function and the logic for each move direction.

### Example Code Snippet:

```python
def add(i1, i2, i3, i4):
    valid = [x for x in [i1, i2, i3, i4] if x != 0]
    result = []
    i = 0

    while i < len(valid):
        if i < len(valid) - 1 and valid[i] == valid[i + 1]:
            result.append(valid[i] * 2)
            i += 2
        else:
            result.append(valid[i])
            i += 1

    # Fill the rest of the list with zeros
    result.extend([0] * (4 - len(result)))

    return result

