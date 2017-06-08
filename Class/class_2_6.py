def search(A, x):#O(n)
    for i in range(len(A)):
        if A[i] == x:
            return i
    return None

def search_2(A, x):#O(n) but destroys list
    if A == []:
        return None
    else:
        if x == A[-1]:
            return len(A)-1
        else:
            '''
            A.pop()
            return search_2(A, x)
            '''
            s = A.pop()
            return search_2(A, x)
            A.append(s)

def search_3(A, x):#O(n^2) but doesnt work
    if A == []:
        return None
    else:
        if x == A[0]:
            return 0
        else:
            return search_3(A[1:], x) + 1#Need +1

def easy_search(A, x, i=0):
    if i == len(A):
        return None
    if A[i] == x:
        return i
    else:
        return easy_search(A, x, i+1)

def binary_search(A, x):#O(logn)
    m = len(A)//2
    if x == A[m]:
        return m
    elif x < A[m]:
        return binary_search(A[:m], x)
    else:
        return binary_search(A[m+1:], x) + m + 1

def bet_binary_search(A, x, l=0, r=None):#l is first half, r is second half
    if r == None:
        r = len(A)
    m = (r-l)//2
    if x == A[m]:
        return m
    elif x < A[m]:
        return bet_binary_search(A, x, l, m-1)
    else:
        return bet_binary_search(A, x, m+1, r)

def flip(A, i=0):#Flip from i on
    if len(A) == i:
        return []
    r = flip(A, i+1)
    r.append(A[i])
    return r

'''
A = [1,2,3]
print( search_2(A, 1) )
print( A)
'''
print (flip([0,1,2,3,4,5,6]))

