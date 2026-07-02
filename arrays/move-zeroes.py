"""
Problem: Move Zeroes
Link: https://leetcode.com/problems/move-zeroes/
Approach: Two pointers. `insert_pos` tracks where the next non-zero
          element should go. Scan through nums, and whenever a non-zero
          is found, swap it into insert_pos and advance insert_pos.
          This preserves relative order and does it in-place.
Time: O(n)   Space: O(1)
"""

def move_zeroes(nums: list[int]) -> None:
    insert_pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1


if __name__ == "__main__":
    nums1 = [0, 1, 0, 3, 12]
    move_zeroes(nums1)
    assert nums1 == [1, 3, 12, 0, 0]

    nums2 = [0]
    move_zeroes(nums2)
    assert nums2 == [0]

    nums3 = [1, 2, 3]
    move_zeroes(nums3)
    assert nums3 == [1, 2, 3]
    print("All test cases passed.")
