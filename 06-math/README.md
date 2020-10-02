# Big-O

From best to worst:
1. O(1): A **constant-time** algorithm does not depend on input size.
2. O(logn): A **logarithmic** algorithms halves the input time at every step.
3. O(n): A **linear** algorithm iterates through input a constant "n" number of times.
4. O(n logn): Usually for sorting.
5. O(n^2): A **quadratic** algorithm contains nested loops.
6. O(n^2 logn)
7. O(n^3)
8. O(2^n): Usually for iterating through all subsets.
9. O(n!): Usually for iterating all permutations.

Note: An exponential function a^n where a > 1 grows faster than any polynomial n^b where b is any constant.

<table>
  <tbody>
    <tr>
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
      <td><a href="01-arrays-and-strings">Array</a></td>
      <td style="color:green">O(1)</td>
      <td align="center" style="color:#CCCC00" colspan="3">O(n)</td>
      <td style="color:green">O(1)</td>
      <td align="center" style="color:#CCCC00" colspan="4">O(n)</td>
    </tr>
    <tr>
      <td><a href="02-linked-lists">Linked List</a></td>
      <td align="center" style="color:#CCCC00" colspan="2">O(n)</td>
      <td align="center" style="color:green" colspan="2">O(1)</td>
      <td align="center" style="color:#CCCC00" colspan="2">O(n)</td>
      <td align="center" style="color:green" colspan="2">O(1)</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td><a href="03-stacks-and-queues">Stack</a></td>
      <td align="center" style="color:#CCCC00" colspan="2">O(n)</td>
      <td align="center" style="color:green" colspan="2">O(1)</td>
      <td align="center" style="color:#CCCC00" colspan="2">O(n)</td>
      <td align="center" style="color:green" colspan="2">O(1)</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td><a href="03-stacks-and-queues">Queue</a></td>
      <td align="center" style="color:#CCCC00" colspan="2">O(n)</td>
      <td align="center" style="color:green" colspan="2">O(1)</td>
      <td align="center" tyle="color:#CCCC00" colspan="2">O(n)</td>
      <td align="center" style="color:green" colspan="2">O(1)</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td>Hash Table</td>
      <td style="color:gray">N/A</td>
      <td align="center" style="color:green" colspan="3">O(1)</td>
      <td style="color:gray">N/A</td>
      <td align="center" style="color:#CCCC00" colspan="4">O(n)</td>
    </tr>
    <tr>
      <td><a href="04-trees-and-graphs">Binary Search Tree</a></td>
      <td align="center" tyle="color:#9acd32" colspan="4">O(log(n))</td>
      <td align="center" style="color:#CCCC00" colspan="5">O(n)</td>
    </tr>
  </tbody>
</table>

<table class="table table-bordered table-striped">
    <tbody>
    <tr>
      <th>Algorithm</th>
      <th colspan="2">Time</th>
      <th>Space</th>
      <th colspan ="2">Comparison</th>
    </tr>
    <tr>
      <th></th>
      <th>Average</th>
      <th>Worst</th>
      <th>Worst</th>
    </tr>
    <tr>
      <td>Bubble Sort</td>
      <td align="center" colspan="2" style="color:red">O(n^2)</td>
      <td style="color:green">O(1)</td>
    </tr>
    <tr>
      <td>Selection Sort</td>
      <td align="center" colspan="2" style="color:red">O(n^2)</td>
      <td style="color:green">O(1)</td>
    </tr>
    <tr>
    <td>Insertion Sort</td>
    <td align="center" colspan="2" style="color:red">O(n^2)</td>
    <td style="color:green">O(1)</td>
    </tr>
    <tr>
    <td>Quicksort</td>
    <td style="color:orange">O(n log(n))</td>
    <td style="color:red">O(n^2)</td>
    <td style="color:#9acd32">O(log(n))</td>
    </tr>
    <tr>
    <td>Mergesort</td>
    <td align="center" colspan="2" style="color:orange">O(n log(n))</td>
    <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
    <td>Heapsort</td>
    <td align="center" colspan="2" style="color:orange">O(n log(n))</td>
    <td style="color:green">O(1)</td>
    </tr>
    <tr>
    <td>Radix Sort</td>
    <td align="center" colspan="2" style="color:green">O(nk)</td>
    <td style="color:#CCCC00">O(n+k)</td>
    </tr>
    </tbody>
</table>


### Sum formulas
Sum of consecutive integers 1 to 100:<br><br>
$\sum_{k=1}^n a = 1 + 2 + 3 + ... + n = \frac{n(n + 1)}{2}$<br><br>
In general: $\sum_{k=1}^n a = 1 + 2 + 3 + ... + n = \frac{(m + n)(n - m + 1)}{2}$

### Arithmetic Progression
An arithmetic progression is a sequence of numbers such that the difference of any two successive members is a constant. <br><br>
If initial term is $a_1$ and the common difference is $d$, then the $n$th term is:<br>
$a_n = a_1 + (n-1)d$<br><br>
So the sum can be derived as: $S_n = \frac{n(a_1 + a_n)}{2}$

### Geometric Progression
In a **geometric sequence** each term is found by multiplying the previous term by a constant. <br><br>
$\sum_{k=0}^{n-1} (ar^k) = a + ar + ar^2 + ... + ar^(n-1) = a \frac{1-r^n}{1-r}$

### Harmonic Sum

### Logarithms
In general: $a = b^c$ transforms to $log_b{a} = c$

# Combinatorics and Probability
**N choose K** is called so because there is (n/k) number of ways to choose k elements, irrespective of their order from a set of n elements.

# P, NP, and NP-Complete
P, NP, and NP-Complete refer to classes of problems. 
- **P** problems are problems that can be quickly solved (where "quickly" means **P**olynomial time). 
- **NP** problems are those where, given a solution, the solution can be quickly verified. 
- **NP-Complete** problems are a subset of NP problems that can all be reduced to each other (that is, if you found a solution to one problem, you could tweak the solution to solve other problems in the set in polynomial time). 
- **NP-Hard** problems are an important set of problems for
which no polynomial algorithm is known.
