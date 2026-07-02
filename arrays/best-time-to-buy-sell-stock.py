"""
Problem: Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Approach: Track the minimum price seen so far while scanning left to right.
          At each day, check the profit if sold today (price - min_price_so_far)
          and keep the maximum profit seen.
Time: O(n)   Space: O(1)
"""

def max_profit(prices: list[int]) -> int:
    min_price = prices[0]
    best_profit = 0

    for price in prices[1:]:
        best_profit = max(best_profit, price - min_price)
        min_price = min(min_price, price)

    return best_profit


if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5   # buy at 1, sell at 6
    assert max_profit([7, 6, 4, 3, 1]) == 0      # prices only fall -> no profit
    assert max_profit([1, 2]) == 1
    print("All test cases passed.")
