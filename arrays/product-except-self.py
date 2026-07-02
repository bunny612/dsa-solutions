"""
Problem: Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/
Approach: For each index, the answer is (product of everything to the left)
          times (product of everything to the right). Build these as prefix
          and suffix products in two passes, without using division.
Time: O(n)   Space: O(1) extra (output array doesn't count)
"""

def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [1] * n

    # First pass: result[i] = product of all elements to the left of i
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Second pass: multiply in product of all elements to the right of i
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    print("All test cases passed.")
