# 3. Longest Substring Without Repeating Characters

**Difficulty:** Medium
**Tags:** `Hash Table` · `String` · `Sliding Window`
**Runtime:** 11 ms (faster than 76.89%)
**Memory:** 19.1 MB (less than 93.76%)
**Source:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

---

## Problem

Given a string `s`, find the length of the **longest** **substring** without duplicate characters.

 

Example 1:**

```

**Input:** s = "abcabcbb"
**Output:** 3
**Explanation:** The answer is "abc", with the length of 3. Note that `"bca"` and `"cab"` are also correct answers.

```

Example 2:**

```

**Input:** s = "bbbbb"
**Output:** 1
**Explanation:** The answer is "b", with the length of 1.

```

Example 3:**

```

**Input:** s = "pwwkew"
**Output:** 3
**Explanation:** The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

 

**Constraints:**

	- `0 <= s.length <= 5 * 104`

	- `s` consists of English letters, digits, symbols and spaces.

## Run

```bash
uv run pytest solutions/0003-longest-substring-without-repeating-characters/
```
