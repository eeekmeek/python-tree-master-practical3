# Computing GCD

def gcd(m, n):
    
    if m > n:
        m, n = n, m
    
    while (n % m != 0):
        n = n % m
        m, n = n, m
    
    return m

print("The greatest common divisor between 24 and 16 is", gcd(24,16))
print("The greatest common divisor between 255 and 25 is", gcd(255,25))

