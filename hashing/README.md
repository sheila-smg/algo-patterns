# Hashing Patterns

Hashing is a technique that maps data to a fixed-size numeric value using a hash function.  
In practice, it allows **constant-time average lookup (O(1))** through data structures such as hash tables.

In Python:
- `dict` implements a hash map (key → value)
- `set` implements a hash set (fast existence checks)

Hashing patterns are used to:
- Count frequencies efficiently  
- Detect whether an element has appeared before  
- Store intermediate state for quick queries  
- Replace nested loops with O(1) lookups  
- Combine hashing with prefix sums for subarray problems  

These patterns often transform problems from **O(n²)** into **O(n)**.

### Common Hashing Use Cases

1. **Frequency Counting**  
   Example problems: anagram check, number of occurrences, Two Sum.

2. **Seen-Before Detection**  
   Example: find the first duplicate, detect cycles, find longest consecutive sequence.

3. **Prefix Hashing**  
   Store cumulative sums in a hash map to quickly detect when a target condition has previously been met.

