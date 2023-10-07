
# Define the sequence a(n) recursively as a(n) = n * a(n-1) + 1 with a(0) = 1
def generate_sequence_a(n):
    a = [1]  # Initialize with a(0) = 1
    for i in range(1, n + 1):
        a.append(i * a[-1] + 1)
    return a

# Generate the sequence a(n) up to n = 463
a_sequence = generate_sequence_a(463)

# Check the user's condition a(p-1) mod p = 0 for each exceptional prime
user_condition_results = {p: a_sequence[p - 1] % p == 0 for p in exceptional_primes}

user_condition_results
