import pandas as pd
from math import factorial
from sympy import isprime

# Function to check if a number is prime (without using sympy)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to generate the user's sequence a(n)
def generate_sequence_a(n):
    a = [1]  # Initialize with a(0) = 1
    for i in range(1, n + 1):
        a.append(i * a[-1] + 1)
    return a

# Function to generate the alternating sum of factorials sequence
def generate_paper_sequence(p):
    s = 0  # Initialize sum
    for i in range(p):
        s += ((-1)**i) * factorial(i)
    return s

# Generate a list of primes from 2 to 60
primes_2_to_60 = [n for n in range(2, 61) if is_prime(n)]

# Check the user's and paper's conditions for each prime in the range 2-60
user_modp_values_2_to_60 = {}
paper_modp_values_2_to_60 = {}

# We can generate the sequence and check the condition on-the-fly to save memory
for p in primes_2_to_60:
    # For user's sequence
    a_value = 1  # Initialize with a(0) = 1
    for n in range(1, p):  # Generate up to a(p-1)
        a_value = n * a_value + 1
    user_modp_values_2_to_60[p] = a_value % p

    # For paper's sequence
    paper_value = sum(((-1)**i) * factorial(i) for i in range(p))
    paper_modp_values_2_to_60[p] = paper_value % p

# Combine the results into a DataFrame
df_modp_2_to_60 = pd.DataFrame({
    'Prime (p)': primes_2_to_60,
    'User Sequence a(p-1) mod p': [user_modp_values_2_to_60[p] for p in primes_2_to_60],
    'Paper Sequence mod p': [paper_modp_values_2_to_60[p] for p in primes_2_to_60]
})

print(df_modp_2_to_60)
