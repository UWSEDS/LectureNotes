"""Functions for finding primes"""

def identify_primes(start_range, end_range):
    result = []
    for candidate in range(start_range, end_range):
        # n is candidate prime. Check if n is prime
        if is_prime(candidate):
            result.append(candidate)
    return(result)

def is_prime(candidate):
    # Return True if number is prime
    is_prime = True
    for m in range(2, candidate):
        if (candidate % m) == 0:
            is_prime = False
    return is_prime
