# 647. Palindromic Substrings

**Difficulty:** Medium
**Tags:** `Two Pointers` · `String` · `Dynamic Programming`
**Runtime:** 627 ms (faster than 10.07%)
**Memory:** 19.3 MB (less than 68.76%)
**Source:** https://leetcode.com/problems/palindromic-substrings/

---

## Problem

Given a string `s`, return *the number of **palindromic substrings** in it*.

A string is a **palindrome** when it reads the same backward as forward.

A **substring** is a contiguous sequence of characters within the string.

 

Example 1:**

```

**Input:** s = "abc"
**Output:** 3
**Explanation:** Three palindromic strings: "a", "b", "c".

```

Example 2:**

```

**Input:** s = "aaa"
**Output:** 6
**Explanation:** Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

```

 

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s` consists of lowercase English letters.

## Run

```bash
uv run pytest solutions/0647-palindromic-substrings/
```
