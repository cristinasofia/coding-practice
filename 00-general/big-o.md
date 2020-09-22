### O(1)
A **constant-time** algorithm does not depend on input size.

### O(logn)
A **logarithmic** algorithms halves the input time at every step.

### O(n)
A **linear** algorithm iterates through input a constant "n" number of times.

### O(n logn)
Usually for sorting.

### O(n^2)
A **quadratic** algorithm contains nested loops.

### O(2^n)
Usually for iterating through all subsets.

### O(n!)
Usually for iterating all permutations.

<table>
    <tbody><tr>
      <th>Data Structure</th>
      <th colspan="8">Time Complexity</th>
      <th>Space Complexity</th>
    </tr>
    <tr>
      <th></th>
      <th colspan="4">Average</th>
      <th colspan="4">Worst</th>
      <th>Worst</th>
    </tr>
    <tr>
      <th></th>
      <th>Access</th>
      <th>Search</th>
      <th>Insertion</th>
      <th>Deletion</th>
      <th>Access</th>
      <th>Search</th>
      <th>Insertion</th>
      <th>Deletion</th>
      <th></th>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Array_data_structure">Array</a></td>
      <td style="color:green">Θ(1)</td>
      <td style="color:#CCCC00">Θ(n)</td>
      <td style="color:#CCCC00">Θ(n)</td>
      <td style="color:#CCCC00">Θ(n)</td>
      <td style="color:green">O(1)</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Stack_(abstract_data_type)">Stack</a></td>
      <td style="color:#CCCC00">Θ(n)</td>
      <td style="color:#CCCC00">Θ(n)</td>
      <td style="color:green">Θ(1)</td>
      <td style="color:green">Θ(1)</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:green">O(1)</td>
      <td style="color:green">O(1)</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Queue_(abstract_data_type)">Queue</a></td>
      <td style="color:#CCCC00">Θ(n)</td>
      <td style="color:#CCCC00">Θ(n)</td>
      <td style="color:green">Θ(1)</td>
      <td style="color:green">Θ(1)</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:green">O(1)</td>
      <td style="color:green">O(1)</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Singly_linked_list#Singly_linked_lists">Singly-Linked List</a></td>
      <td style="color:#CCCC00">Θ(n)</td>
      <td style="color:#CCCC00">Θ(n)</td>
      <td style="color:green">Θ(1)</td>
      <td style="color:green">Θ(1)</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:green">O(1)</td>
      <td style="color:green">O(1)</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Doubly_linked_list">Doubly-Linked List</a></td>
      <td style="color:#CCCC00">Θ(n)</td>
      <td style="color:#CCCC00">Θ(n)</td>
      <td style="color:green">Θ(1)</td>
      <td style="color:green">Θ(1)</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:green">O(1)</td>
      <td style="color:green">O(1)</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Hash_table">Hash Table</a></td>
      <td style="color:gray">N/A</td>
      <td style="color:green">Θ(1)</td>
      <td style="color:green">Θ(1)</td>
      <td style="color:green">Θ(1)</td>
      <td style="color:gray">N/A</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Binary_search_tree">Binary Search Tree</a></td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:#CCCC00">O(n)</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Red-black_tree">Red-Black Tree</a></td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">O(log(n))</td>
      <td style="color:#9acd32">O(log(n))</td>
      <td style="color:#9acd32">O(log(n))</td>
      <td style="color:#9acd32">O(log(n))</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td><a href="https://en.wikipedia.org/wiki/Splay_tree">Splay Tree</a></td>
      <td style="color:gray">N/A</td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:gray">N/A</td>
      <td style="color:#9acd32">O(log(n))</td>
      <td style="color:#9acd32">O(log(n))</td>
      <td style="color:#9acd32">O(log(n))</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/AVL_tree">AVL Tree</a></td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">Θ(log(n))</td>
      <td style="color:#9acd32">O(log(n))</td>
      <td style="color:#9acd32">O(log(n))</td>
      <td style="color:#9acd32">O(log(n))</td>
      <td style="color:#9acd32">O(log(n))</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
</tbody></table>

<table class="table table-bordered table-striped">
    <tbody><tr>
      <th>Algorithm</th>
      <th colspan="3">Time Complexity</th>
      <th>Space Complexity</th>
    </tr>
    <tr>
      <th></th>
      <th>Best</th>
      <th>Average</th>
      <th>Worst</th>
      <th>Worst</th>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Quicksort">Quicksort</a></td>
      <td style="color:orange">Ω(n log(n))</td>
      <td style="color:orange">Θ(n log(n))</td>
      <td style="color:red">O(n^2)</td>
      <td style="color:#9acd32">O(log(n))</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Merge_sort">Mergesort</a></td>
      <td style="color:orange">Ω(n log(n))</td>
      <td style="color:orange">Θ(n log(n))</td>
      <td style="color:orange">O(n log(n))</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Timsort">Timsort</a></td>
      <td style="color:#CCCC00">Ω(n)</td>
      <td style="color:orange">Θ(n log(n))</td>
      <td style="color:orange">O(n log(n))</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Heapsort">Heapsort</a></td>
      <td style="color:orange">Ω(n log(n))</td>
      <td style="color:orange">Θ(n log(n))</td>
      <td style="color:orange">O(n log(n))</td>
      <td style="color:green">O(1)</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Bubble_sort">Bubble Sort</a></td>
      <td style="color:#CCCC00">Ω(n)</td>
      <td style="color:red">Θ(n^2)</td>
      <td style="color:red">O(n^2)</td>
      <td style="color:green">O(1)</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Insertion_sort">Insertion Sort</a></td>
      <td style="color:#CCCC00">Ω(n)</td>
      <td style="color:red">Θ(n^2)</td>
      <td style="color:red">O(n^2)</td>
      <td style="color:green">O(1)</td>
    </tr>
    <tr>
      <td><a href="https://en.wikipedia.org/wiki/Tree_sort">Tree Sort</a></td>
      <td style="color:orange">Ω(n log(n))</td>
      <td style="color:orange">Θ(n log(n))</td>
      <td style="color:red">O(n^2)</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Shellsort">Shell Sort</a></td>
      <td style="color:orange">Ω(n log(n))</td>
      <td style="color:red">Θ(n(log(n))^2)</td>
      <td style="color:red">O(n(log(n))^2)</td>
      <td style="color:green">O(1)</td>
    </tr>
    <tr>
      <td><a rel="tooltip" title="Constant number of digits 'k'" href="http://en.wikipedia.org/wiki/Radix_sort">Radix Sort</a></td>
      <td style="color:green">Ω(nk)</td>
      <td style="color:green">Θ(nk)</td>
      <td style="color:green">O(nk)</td>
      <td style="color:#CCCC00">O(n+k)</td>
    </tr>

  </tbody>
</table>
