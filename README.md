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

\[ u_{n+1} = -1 + (n+1)u_n \]
initialized with:
\[ u_0 = e - 1 \]
... this (when symbolically calculated) forms:

- **Integers (\( n \))**: The index \( n \) in the sequence progression represents natural counting, starting from 0.

#### Factorials
- The sequence generates terms that feature factorial growth when associated with the number \( e \). Specifically, the coefficient of \( e \) in each term is \( n! \), indicating that the term captures the factorial nature of \( n \), scaled by \( e \).

#### Arrangements
- The negative component in each term of the sequence signifies the total number of arrangements possible for a set of \( n \) distinct objects. These arrangements include all permutations of subsets of an \( n \)-set, which is also the number of one-to-one sequences that can be formed from \( n \) distinct objects.
  - The sequence for these negative components is: 1, 2, 5, 16, 65, 326, 1957, 13700, ...

The negative components can be understood as the sum of permutations of all subsets of an \( n \)-set, including the empty set. This can be defined mathematically as:
\[ a(n) = \sum_{k=0}^{n} \frac{n!}{k!} \]
This is the total number of one-to-one sequences that can be formed from \( n \) distinct objects, including sequences with zero elements (i.e., the empty set).

### Synthesis
 sequence encapsulates two distinct mathematical properties:
1. **Factorial Growth**: The positive part of each term captures the factorial nature of \( n \), scaled by \( e \).
2. **Combinatorial Counting**: The negative component of each term represents the total number of permutations of all subsets of an \( n \)-set, following the sum \( a(n) = \sum_{k=0}^{n} \frac{n!}{k!} \).

This sequence is a fascinating blend of both exponential and combinatorial growth, making it rich for analysis in both calculus and combinatorial mathematics.

