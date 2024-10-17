# Bit by Bit Problem

## Problem Description
This script implements a solution for a [Bit by Bit Problem](https://open.kattis.com/problems/bitbybit).
A brand new Ultra-CISC microprocessor has a collection of instructions for manipulating individual bits of one of its 32-bit registers. The instructions work as described in the following table. In all cases, bit 0 is the low-order bit and bit 31 is the high-order bit. The representation of the instruction set makes it impossible to try to manipulate bits outside this range.

| Instruction | Description |
|-------------|-------------|
| CLEAR i     | Put a zero into bit i. |
| SET i       | Put a one into bit i. |
| OR i j      | Store in bit i the logical OR of the contents of bits i and j. |
| AND i j     | Store in bit i the logical AND of the contents of bits i and j. |

Your job is to determine the contents of the register after a sequence of these operations. Unfortunately, you don't know anything about what was in the register before the instructions.

## Input
Input consists of multiple instruction sequences, each beginning with a positive integer n ≤ 100. This is followed by n lines, each giving a legal bit manipulation instruction. All bits referenced are in the range 0 - 31 (inclusive). The end of input is marked with a value of 0 for n.

## Output
For each instruction sequence, print out a line giving the final contents of the register. Print your result in binary, with the most significant bit on the left. Since you don't know anything about what was in the register before the instructions, just print a question mark for those bits whose values you can't determine.

## Solution Approach
1. Initialize a list of length 32 with all elements set to -1 to represent the unknown state of the register.
2. For each instruction in the sequence:
   - If the instruction is "SET", set the corresponding bit to 1.
   - If the instruction is "CLEAR", set the corresponding bit to 0.
   - If the instruction is "AND", update the corresponding bit based on the logical AND of the current bit and the referenced bit.
   - If the instruction is "OR", update the corresponding bit based on the logical OR of the current bit and the referenced bit.
3. After processing all instructions, replace -1 with '?' for unknown bits and join the list to form the final binary representation.

## Code Explanation
```python
result = []
while True:
    temp = input()
    if temp == "0":
        break
    if temp.isdigit():
        temp_ls = [-1] * 32
        command = []
        for _ in range(int(temp)):
            command.append(input().split())

        for item in command:
            i = 31 - int(item[1])
            if item[0] == "SET":
                temp_ls[i] = 1
            if item[0] == "CLEAR":
                temp_ls[i] = 0
            if item[0] == "AND":
                j = 31 - int(item[2])
                if temp_ls[i] == 1 and temp_ls[j] == 1:
                    temp_ls[i] = 1
                elif temp_ls[i] == 0 or temp_ls[j] == 0:
                    temp_ls[i] = 0
                else:
                    temp_ls[i] = -1
            if item[0] == "OR":
                j = 31 - int(item[2])
                if temp_ls[i] == 1 or temp_ls[j] == 1:
                    temp_ls[i] = 1
                elif temp_ls[i] == 0 and temp_ls[j] == 0:
                    temp_ls[i] = 0
                else:
                    temp_ls[i] = -1

        result.append(temp_ls)

for item in result:
    item = ["?" if x == -1 else str(x) for x in item]
    print("".join(item))
```

1. We initialize an empty list `result` to store the final state of the register for each instruction sequence.
2. We start a loop that continues until the input is "0".
3. For each instruction sequence:
   - We initialize a list `temp_ls` of length 32 with all elements set to -1 to represent the unknown state of the register.
   - We read the instructions and store them in the `command` list.
   - We iterate over each instruction in `command`:
     - If the instruction is "SET", we set the corresponding bit (indexed from the right) to 1.
     - If the instruction is "CLEAR", we set the corresponding bit to 0.
     - If the instruction is "AND", we update the corresponding bit based on the logical AND of the current bit and the referenced bit.
     - If the instruction is "OR", we update the corresponding bit based on the logical OR of the current bit and the referenced bit.
   - After processing all instructions, we append the final state of the register (`temp_ls`) to the `result` list.
4. Finally, we iterate over each item in `result`, replace -1 with '?' for unknown bits, and print the final binary representation.

## Time Complexity
The time complexity of this solution is O(n * m), where n is the number of instruction sequences and m is the maximum number of instructions in a sequence. We iterate over each instruction sequence and process each instruction within that sequence.

## Space Complexity
The space complexity is O(n * m) as well, since we store the instructions for each sequence in the `command` list and the final state of the register for each sequence in the `result` list.

