def sqrt(N):
    N = N * 1.0 # un-int the number
    old_guess = -1
    guess = 1
    while abs(guess-old_guess) > 0.01:  # 0.01 is the precision
        old_guess = guess
        guess = (guess + N/guess) / 2

    return guess

print(sqrt(2))
