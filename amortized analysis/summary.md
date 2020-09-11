## Sliding Window
Start grows in inner loop and end grows in outer loop.
Counter used for problem specification.
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