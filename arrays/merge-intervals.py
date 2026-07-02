"""
Problem: Merge Intervals
Link: https://leetcode.com/problems/merge-intervals/
Approach: Sort intervals by start time. Walk through them, and if the
          current interval overlaps with the last merged one (its start
          is <= the last one's end), merge them by extending the end.
          Otherwise, start a new interval.
Time: O(n log n) — dominated by sorting   Space: O(n) for the result
"""

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda pair: pair[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if start <= last_end:
            # Overlaps with the last interval -> extend it
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged


if __name__ == "__main__":
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge_intervals([[1, 4]]) == [[1, 4]]
    print("All test cases passed.")
