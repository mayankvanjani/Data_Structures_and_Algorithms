def min(A):
    x = A[0] #runtime: 1 run once
    for y in A:
        if y<x:#runtime: b run n times
            x = y:#runtime: c run 0-N times
    return x;#runtime: d run once
# O(n)



