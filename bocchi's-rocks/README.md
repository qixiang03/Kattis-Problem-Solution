# Bocchi's Rocks

This is a Python solution to the ["Bocchi's Rocks" problem on Kattis](https://open.kattis.com/problems/bocchinorokku). 

## Problem Description

Bocchi has a collection of N rocks of different weights. For each rock in her collection, Bocchi wants to know the amount of the other rocks that weigh less than the actual rock.

## Input

The input consists of:
- The first row is a single integer, N (1 ≤ N ≤ 2 · 10^5), amount of rocks that Bocchi has in her collection. 
- The second row contains N integers, where the ith integer wi (1 ≤ wi ≤ 10^9) is the weight of the ith rock, for all 1 ≤ i ≤ N.

It is guaranteed that the weights of all rocks are different.

## Output 

Output N integers on the same row, where the ith integer is the number of rocks that weigh less than the ith rock.

## Solution

```python
no_of_rock = int(input())
rocks = [int(x) for x in input().split()]
indexed_rocks = [(weight, index) for index, weight in enumerate(rocks)]

indexed_rocks.sort()

result = [0]*no_of_rock

for rank, (weight, ori_index) in enumerate(indexed_rocks):
    result[ori_index] = rank


print(" ".join(map(str, result)))
```

## Explanation

1. Read in the number of rocks (`no_of_rock`) and the weights of each rock (`rocks`).
2. Create a list of tuples `indexed_rocks`, where each tuple contains the weight and original index of a rock. This is to keep track of the original positions after sorting.
3. Sort `indexed_rocks` by weight. After sorting, the index of each tuple represents how many rocks are lighter than it.
4. Create a `result` list of length `no_of_rock` initialized with zeros. This will store the final answer.
5. Iterate through the sorted `indexed_rocks`. For each rock:
   - `rank` is the index in the sorted list, which equals the number of rocks lighter than the current rock.
   - `ori_index` is the original index of this rock.
   - Assign `rank` to `result[ori_index]`, putting the number of lighter rocks in the correct position.
6. Print out the `result` list.

## Complexity Analysis

- Time Complexity: O(N log N) due to the sorting operation. The hardest part is breaking down the seemingly N^2 time complexity to N log N, to pass the Group 2 test cases. Using the original nested loop approach would exceed the time limit.
- Space Complexity: O(N) to store the `indexed_rocks` and `result` lists.

## Points and Test Cases

This solution passes all test case groups on Kattis:
- Group 1 (10 points): N ≤ 2 
- Group 2 (40 points): N ≤ 1000
- Group 3 (50 points): No further constraints

The key is optimizing the time complexity to O(N log N) using sorting, to handle the larger input sizes in Groups 2 and 3 within the time limit.
