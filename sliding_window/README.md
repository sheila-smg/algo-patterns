# Sliding Window

The sliding window technique is a powerful pattern for processing contiguous segments of data in linear time.  
It replaces repeated work with a dynamic “window” that expands, contracts or moves across the input while maintaining just enough state to answer the problem efficiently.

Sliding window is used when:
- The problem involves **continuous segments** of an array or string.
- You need to track something like a sum, count, frequency or condition **as the window moves**.
- A brute-force solution would recompute the same work many times.

This pattern often reduces solutions from O(n·k) or O(n²) to **O(n)**.


## Types of Sliding Windows

Sliding windows can be organized into three main categories:

### 1. **Fixed Window**
A window with a constant size `k`.  
Typical use cases:
- Maximum sum of subarray with length k  
- Maximum average subarray  
- Counting windows that satisfy a condition of fixed length  

The key idea is updating the state by:
- Subtracting the element that leaves the window  
- Adding the new element that enters  


### 2. **Variable Window**
A window that grows or shrinks depending on a condition.  
Used when the requirement is dynamic, not tied to a constant k.

Examples:
- Longest substring without repeating characters  
- Longest substring with at most k distinct characters  

The logic:
- Expand the window by moving the right pointer  
- If invalid, shrink it by moving the left pointer  
- Track the best valid window seen so far  


### 3. **Frequency Window**
A window that relies on **frequency maps** or Counters.  
Typical when the problem involves matching character frequencies.

Examples:
- Find all anagrams in a string  
- Minimum window substring  
- Count substrings matching a pattern’s distribution  

This pattern uses:
- Frequency of the target  
- Frequency of the current window  
- Incremental updates as the window moves  


## Why Sliding Window Matters

Most problems involving continuous ranges can be reframed as sliding window problems.  
Understanding the variations makes it easy to:
- Identify unnecessary repeated work  
- Track only what changes between steps  
- Move from O(n²) approaches to elegant linear-time solutions  

This folder contains structured examples for each category:
- A conceptual explanation  
- A simple baseline version  
- An optimized implementation  
- Notes highlighting the reasoning and complexity insights  