# A Cappella Recording Problem

## Problem Description

Geoffry is preparing an a cappella composition where he sings the entire song by himself. Each note of the song has a pitch between 0 and 10^9. Due to the varying pitches, Geoffry will record himself singing multiple times. In a single recording, he will sing a subset of notes within a limited pitch range to avoid straining his voice.

The task is to compute the minimum number of recordings Geoffry needs to make to ensure each note is sung in at least one recording.

## Input

- The first line contains two integers `n` and `d` (1 ≤ n ≤ 10^5, 0 ≤ d ≤ 10^9):
  - `n` is the number of notes in Geoffry's song
  - `d` is the largest difference between the minimum and maximum pitch that Geoffry can handle in a single recording
- Each of the next `n` lines contains a single integer `p` (0 ≤ p ≤ 10^9), representing the pitch of each note in the order they are to be sung

## Output

A single integer, which is the minimum number of recordings that Geoffry needs to make.

## Approach

1. Sort the notes by pitch
2. Iterate through the sorted notes
3. For each note, find the maximum number of subsequent notes that fall within the pitch range `d`
4. Move to the next note outside this range and repeat
5. Count the number of such groups, which represents the minimum number of recordings

## Solution

```python
no_of_input, diff = [int(x) for x in input().split()]
notes = []
for _ in range(no_of_input):
    notes.append(int(input()))
notes = sorted(notes)
i = 0
count = 1  # Start with one group by default
while i < len(notes):
    max_value = notes[i] + diff
    for j in range(i + 1, len(notes)):
        if notes[j] > max_value:
            i = j
            count += 1
            break
    else:
        break
print(count)
```

## Explanation

1. We start by reading the input: number of notes and the maximum pitch difference allowed.
2. We then read all the note pitches and store them in a list.
3. The notes are sorted in ascending order of pitch.
4. We initialize a counter to 1, assuming we'll need at least one recording.
5. We iterate through the sorted notes:
   - For each note, we calculate the maximum pitch allowed in this recording (`max_value = notes[i] + diff`).
   - We then look for the first note that exceeds this maximum pitch.
   - If we find such a note, we start a new recording (increment `count`) and continue from this note.
   - If we don't find such a note, it means all remaining notes fit in the current recording, so we're done.
6. Finally, we print the total number of recordings needed.

This greedy approach ensures that we always include the maximum number of notes possible in each recording, thus minimizing the total number of recordings needed.

## Time Complexity

- Sorting the notes: O(n log n)
- Iterating through the notes: O(n) in the worst case

Overall time complexity: O(n log n), where n is the number of notes.

## Space Complexity

O(n) to store the list of notes.


