def bad_merge(A, B):
    if len(A) == 0:
        return B
    if len(B) == 0:
        return A
    if A[0] < B[0]:
        return [A[0]] + merge(A[1:], B)
    else:
        return [B[0]] + merge(A, B[1:])

def merge(A, B):
    if len(A) == 0:
        return B
    if len(B) == 0:
        return B
    if A[-1] > B[-1]:
        p = A.pop()
        l = merge(A, B)
        l.append(p)
        return l
    else:
        p = B.pop()
        l = merge(A, B)
        l.append(p)
        return l

def merge_sorted(A):
    if len(A) <= 1:
        return A
    return merge(merge_sorted(A[:len(A)//2]), merge_sorted(A[len(A)//2:]))
        
    
    
