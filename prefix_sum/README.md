# Prefix Sum

## What is a Prefix Sum?

A prefix sum is an array where each position stores the cumulative sum of elements up to that index.

We define it as:

    prefix[0] = 0
    prefix[i] = nums[0] + nums[1] + ... + nums[i-1]

This definition makes range queries and subarray problems easier and less error-prone.

---

## When should I think of Prefix Sum?

Think of prefix sums whenever you see:

- Subarrays or ranges
- Sum between indices `i` and `j`
- Conditions involving cumulative values
- Balanced states (e.g. sum, count, difference)
- Negative numbers that break sliding window assumptions

Key signal:  
"Sum of a subarray" + negative numbers → Prefix sum + hashmap

---

## Core Insight

The sum of a subarray from index `i` to `j` can be written as:

    sum(i, j) = prefix[j + 1] - prefix[i]

Rearranged:

    prefix[i] = prefix[j + 1] - target

This means that for each prefix sum, we only need to know how many times we have seen a specific previous prefix value.

---

## Typical Pattern: Subarray Sum Equals k

### Why sliding window fails

Sliding window only works when all numbers are non-negative.  
With negative numbers, expanding the window does not guarantee monotonic growth.

### Why prefix sum works

Prefix sums transform a subarray problem into a lookup problem over past states.

### Algorithm

1. Initialize a hashmap to count prefix sums
2. Start with `{0: 1}` to handle subarrays starting at index 0
3. Iterate through the array, maintaining a running sum
4. For each position, check if `(current_sum - k)` exists in the hashmap
5. Add its frequency to the result
6. Update the hashmap with the current sum

---

## Common Mistakes

- Forgetting to initialize `{0: 1}`
- Updating the hashmap before counting valid subarrays
- Using sliding window with negative numbers
- Off-by-one errors in prefix definition

---

## Complexity

- Time complexity: O(n)
- Space complexity: O(n)

---

## Mental Checklist

Before coding, ask yourself:

- Am I dealing with subarrays or ranges?
- Are there negative numbers?
- Can I express the condition as `prefix[j] - prefix[i] = k`?
- Do I need a hashmap to track previous states?

If yes, this is a prefix sum problem.

