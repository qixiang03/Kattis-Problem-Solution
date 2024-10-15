# 99 Problems Solver

This script solves the [99 Problems problem](https://open.kattis.com/problems/99problems) where the goal is to find the nearest positive integer ending in 99 for a given product price `N`. If two such numbers are equally close, the bigger one should be returned.

## Problem Description

Ingrid is a founder of a company that sells bicycle parts. She has decided that prices ending in 99 are more profitable, so given a product price `N`, your task is to find the nearest price ending in 99.

### Input Format

- A single integer `N` (1 ≤ N ≤ 10,000), the price of a product. It is guaranteed that `N` does not end in 99.

### Output Format

- A single integer, the closest positive integer that ends in 99.
- If two such numbers are equally close, return the larger one.

## Approach

1. **Handle small values**: If `N` is less than or equal to 99, the nearest price ending in 99 is simply 99.
2. **For larger values**: The algorithm iterates over potential prices that end in 99 by appending `99` to increasing integers.
3. **Check proximity**: For each candidate price, the program checks whether `N` falls within a range of ±50 around that candidate price. If it does, the candidate price is printed.

## Code Explanation

The main logic checks for potential prices ending in `99` and compares them to `N` based on proximity.

### Example Code Snippet:

```python
string = "99"
val = int(input())

for i in range(1000):

    if val <= 99:
        print(99)
        break

    temp = int(str(i) + string)
    if temp - 50 <= val < temp + 50:
        print(temp)
        break
