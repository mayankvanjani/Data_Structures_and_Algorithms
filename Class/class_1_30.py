def pow(a, n):
    if (n==0):
        return 1
    else:
        return a * pow(a, n-1)

print( pow(2, 5) )

def diff_pow(a, n):
    if (n==0):
        return 1
    else:
        if (n%2 == 0):
            return pow(a, n//2) * pow(a, n//2)
        else:
            return a * pow(a, n//2) * pow(a, n//2)

def better_pow(a, n):
    if (n==0):
        return 1
    else:
        p = pow(a, n//2)
        if (n%2 == 0):
            return p*p
        else:
            return a*p*p

print(better_pow(2, 1000000))
