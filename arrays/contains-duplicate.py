"""
Problem: Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Approach: Add elements to a hash set as we scan. If an element is already
          in the set, a duplicate exists.
Time: O(n)   Space: O(n)
"""

def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([]) is False
    print("All test cases passed.")
