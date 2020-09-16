## Sliding Window
Start grows in inner loop and end grows in outer loop. <br>
Counter used for problem specification. <br>
<pre>
    <code>
    start, end = 0, 0
    dict = {}
    count = 0

    while end < len(arr):
    
    dict[end] += 1
    if dict[end] :
        count += 1

    end += 1
    
    while count :
        # update result if finding min
        min_len = min(min_len, end – start + 1)
        
        dict[start] -= 1
        if dict[start] :
        count -= 1

        start += 1

    # update result if finding maximum
    max_len = max(max_len, end – start)
    </code>
</pre>

[Min Window Substring](https://leetcode.com/problems/minimum-window-substring/)<br>
[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)<br>
[Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)<br>
[Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)<br>
[Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)<br>
[Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)<br>
[Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)<br>

## Fast and Slow
Fast pointer moves through same array at greater pace than slow. <br>
<pre>
    <code>
    slow = arr[0]

    for fast in range(arr):
    if slow condition:
        slow = slow.next # slow += 1
    </code>
</pre>

[Remove Duplicates](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)<br>
[Remove N-th Node](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)<br>

## Old and New State Pointers
1.	Calculate current result based on old state value (compare).
2.	Before assigning current result, store old state value into new state.
3.	Now current state proceed as new state.
<pre>
    <code>
    last, now = 0, 0

    for i in arr:
    last, now = now, max(last + i, now)

    return now
    </code>
</pre>

[Fib](https://leetcode.com/problems/fibonacci-number/)<br>
[House Robber](https://leetcode.com/problems/house-robber/)<br>
[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)<br>
[Decode Ways](https://leetcode.com/problems/decode-ways/ )<br>

## Left and Right Pointers
1.	One pointer on beginning (left), one pointer on end (right)
2.	Move toward each other until meet in middle
<pre>
    <code>
    l, r = 0, len(arr) – 1

    while l < r:
    if left condition:
        l += 1
    if right condtion:
        r -= 1
    </code>
</pre>

[Two Sum](https://leetcode.com/problems/two-sum/)<br>
[Container with Most Water](https://leetcode.com/problems/container-with-most-water/)

## Two Pointers
Each pointer moves independently.
<pre>
    <code>
    p1, p2 = 0, 0

    while p1 < len(arr1) and p2 < len(arr2):
    if arr1 condition:
        p1 += 1
    if arr2 condition:
        p2 += 1
    </code>
</pre>

[Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)