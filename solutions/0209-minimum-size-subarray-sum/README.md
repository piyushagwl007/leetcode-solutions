# 209. Minimum Size Subarray Sum

**Difficulty:** Medium
**Tags:** `Array` · `Binary Search` · `Sliding Window` · `Prefix Sum`
**Runtime:** 11 ms (faster than 49.07%)
**Memory:** 30.6 MB (less than 18.10%)
**Source:** https://leetcode.com/problems/minimum-size-subarray-sum/

---

## Problem

Given an array of positive integers `nums` and a positive integer `target`, return *the **minimal length** of a **subarray** whose sum is greater than or equal to* `target`. If there is no such subarray, return `0` instead.

 

Example 1:**

```

**Input:** target = 7, nums = [2,3,1,2,4,3]
**Output:** 2
**Explanation:** The subarray [4,3] has the minimal length under the problem constraint.

```

Example 2:**

```

**Input:** target = 4, nums = [1,4,4]
**Output:** 1

```

Example 3:**

```

**Input:** target = 11, nums = [1,1,1,1,1,1,1,1]
**Output:** 0

```

 

**Constraints:**

	- `1 <= target <= 109`

	- `1 <= nums.length <= 105`

	- `1 <= nums[i] <= 104`

 

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution of which the time complexity is `O(n log(n))`.

## Run

```bash
uv run pytest solutions/0209-minimum-size-subarray-sum/
```
