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
