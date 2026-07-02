"""
Problem: Maximum Subarray (Kadane's Algorithm)
Link: https://leetcode.com/problems/maximum-subarray/
Approach: At each index, decide whether to extend the previous subarray
          or start a new one from the current element — whichever gives
          a larger sum. Track the best sum seen so far separately.
Time: O(n)   Space: O(1)
"""

def max_subarray(nums: list[int]) -> int:
    current_sum = nums[0]
    best_sum = nums[0]

    for num in nums[1:]:
        # Either extend the running subarray, or start fresh at num
        current_sum = max(num, current_sum + num)
        # Update the overall best if this is better
        best_sum = max(best_sum, current_sum)

    return best_sum


if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    assert max_subarray([-1, -2, -3]) == -1  # all negative -> single max element
    print("All test cases passed.")
