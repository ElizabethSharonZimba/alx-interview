#!/usr/bin/python3
def isWinner(x, nums):
    max_num = max(nums)
    prime_numbers = sieve_of_eratosthenes(max_num)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        primes_in_round = [p for p in prime_numbers if p <= n]
        current_player = "Mama"
        
        while primes_in_round:
            prime = primes_in_round[0]
            primes_in_round = [p for p in primes_in_round if p % prime != 0]
            
            if current_player == "Mama":
                current_player = "Baby"
            else:
                current_player = "Mama"
        
        if current_player == "Baby":
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Mama"
    elif ben_wins > maria_wins:
        return "Baby"
    else:
        return None
