# Peculiar-Primes

A Paper from 2009 found an interesting connection to the Taylor Series https://browse.arxiv.org/pdf/0709.0671.pdf



<img width="599" alt="image" src="https://github.com/jconorgrogan/Peculiar-Primes/assets/130090573/4c69a713-d087-4a16-a11c-775197d23f5b">

I have found a seperate function that generates these primes as well

<img width="445" alt="image" src="https://github.com/jconorgrogan/Peculiar-Primes/assets/130090573/588456b0-3bed-44d6-bd9a-64a9c062a708">

<img width="603" alt="image" src="https://github.com/jconorgrogan/Peculiar-Primes/assets/130090573/f0781052-ff2e-4c24-94c6-0669f1fd84dc">

# Modulo \( p \) Analysis of Two Different Mathematical Constructs

## Conor's Sequence \( a(n) \)

### Equation
\[ a(n) = n \cdot a(n-1) + 1 \]
\[ a(n) \mod p = (n \cdot a(n-1) + 1) \mod p \]

### Characteristics
1. **Recursive Sequence**: Each term depends on the previous term.
2. **Multiplicative Structure**: Involves multiplication by integers.
3. **Addition of 1**: Each term is incremented by 1.
4. **Defined for All Natural Numbers**: The sequence is generated for all \( n \).

---

## Paper's Sequence \( S \)

### Equation
\[ S = 1 - 1! + 2! - 3! + \ldots + (-1)^{p-1} \cdot (p-1)! \]
\[ S \mod p = \sum_{i=0}^{p-1} (-1)^i \cdot i! \mod p \]

---

## Common Observation

Despite being fundamentally different, both \( a(n) \) and \( S \) yield the same modulo \( p \) values for prime \( p \).

.....
This formula feels very similar to another interesting set of relationships:

[ u_{n+1} = -1 + (n+1)u_n \]
initialized with:
\[ u_0 = e - 1 \]... this forms:

1. **Integers (n)**: The index \( n \) in the sequence progression represents the natural counting of integers.

2. **Factorials**: The sequence produces values that, when associated with the number \( e \), reveal factorial growth. Each term in the sequence, when considered in terms of \( e \), captures the factorial of the integer \( n \), albeit scaled by \( e \).

3. **Arrangements**: The negative component in each term of the sequence represents the count of possible arrangements or configurations for the respective integer \( n \). Specifically, The negative number is Total number of permutations of all subsets of an n-set (and the number of one-to-one sequences that can be formed from n distinct objects). You see this sequence, with a negative sign in the output:	1, 2, 5, 16, 65, 326, 1957, 13700,


...Compared to the first sequence discussed, One sequence "adds then multiplies," and the other "multiplies then subtracts," and they do so with slightly adjusted scaling factors (
�
n vs. 
�
+
1
n+1).

