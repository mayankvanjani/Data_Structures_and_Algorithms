'''
Mayank Vanjani mv1506
Homework 2
2/5/17
'''

#C-4.9
def rec_min_max(lst, curr=None, minim=0, maxim=0):
    if curr == None: #Initialize
        curr = 0
        minim = lst[0]
        maxim = lst[0]
    if curr == len(lst): #Base Case
        return ("Min: "+str(minim), "Max: "+str(maxim))
    
    if lst[curr] < minim:
        return rec_min_max(lst, curr+1, lst[curr], maxim)
    elif lst[curr] > maxim:
        return rec_min_max(lst, curr+1, minim, lst[curr])
    else:
        return rec_min_max(lst, curr+1, minim, maxim)

#C-4.10
def int_part(n, ints=1):
    if n < 2 and ints == 1: #Special Case
        return 0
    if n // 2 < 2: #Base Case
        return ints

    return int_part(n // 2, ints + 1)

#C-4.11
def elem_uniqueness(A, curr = 0, r = None):
    if r == None: #Initialize
        r = len(A)
    if curr + 1 == r:
        return True

    return (elem_uniqueness(A,curr+1,r) and
            elem_uniqueness(A,curr,r-1) and
            A[curr]!=A[r-1])
    
#C-4.15
def subset_of_set(lst):
    if len(lst) == 0:
        return [[]]
    temp = subset_of_set(lst[1:])
    return temp + [[lst[0]] + x for x in temp]

#C-4.17
def is_palindrome(s, start=0, end=None):
    if end == None: #Init
        end = len(s)-1
    if start>end: #Base Case
        return True

    return (s[start] == s[end] and
            is_palindrome(s, start+1, end-1))

#C-4.20
def rearrange(S, k, ans = [], curr = 0):
    if curr == len(S): #Base Case
        return ans

    if S[curr] <= k:
        ans = [S[curr]] + ans
    else:
        ans.append(S[curr])
    return rearrange(S, k, ans, curr+1)
        

def main():
    lst = [-1, -5, 7]
    ls = [2, 18, -100, 5, 1, 1, 2, 0]
    print( lst, rec_min_max(lst) )
    print( ls, rec_min_max(ls) )
    print()
    
    print( "Integer part of base 2 log of", 1000, "is", int_part(1000) )
    print( "Integer part of base 2 log of", 2, "is", int_part(2) )
    print( "Integer part of base 2 log of", 1, "is", int_part(1) )
    print()

    lst2 = [1, 5, 7, 4, 4]
    lst3 = [4, 2, 5, 8, 9]
    lst4 = [10, 2, 3, 4, 10]
    print( lst2, "Unique?", elem_uniqueness(lst2) )
    print( lst3, "Unique?", elem_uniqueness(lst3) )
    print( lst4, "Unique?", elem_uniqueness(lst4) )
    print()

    sets = [1, 2, 3]
    sets2 = [1,2,3,4]
    print(subset_of_set(sets))
    print(subset_of_set(sets2))
    print()

    palin1 = "racecar"
    palin2 = "gohangasalamiimalasagnahog"
    palin3 = "testfalse"
    print( palin1, "Palindrome?", is_palindrome(palin1) )
    print( palin2, "Palindrome?", is_palindrome(palin2) )
    print( palin3, "Palindrome?", is_palindrome(palin3) )
    print()

    S = [9,6,4,2,6,4,5,7,9,10]
    k = 5
    print( "S =", S, "K =", k)
    print( rearrange(S, k) )

main()
