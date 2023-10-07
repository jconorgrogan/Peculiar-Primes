# Peculiar-Primes

A Paper from 2009 found an interesting connection to the Taylor Series https://browse.arxiv.org/pdf/0709.0671.pdf
<img width="640" alt="image" src="https://github.com/jconorgrogan/Peculiar-Primes/assets/130090573/4535f262-e0e2-432d-bff0-aa2041e6feba">


<img width="599" alt="image" src="https://github.com/jconorgrogan/Peculiar-Primes/assets/130090573/4c69a713-d087-4a16-a11c-775197d23f5b">

I have found a seperate function that generates these primes as well

<img width="445" alt="image" src="https://github.com/jconorgrogan/Peculiar-Primes/assets/130090573/588456b0-3bed-44d6-bd9a-64a9c062a708">

<img width="602" alt="image" src="https://github.com/jconorgrogan/Peculiar-Primes/assets/130090573/6ff89a39-f241-4d0c-9be6-9205561ea422">

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
