def f(x,n):
    ans = 0
    for i in range(n+1):
        tempans = 1
        for j in range(i):
            tempans *= x
        ans += tempans
    return ans
print("Question 1")
print(f(2,3),"\n")

class counter:
    def __init__(self):
        self._i = 0
    def print_and_increment(self):
        print(self._i)
        self._i = self._i + 1
print("Question 6")
c = counter()
c.print_and_increment()
c.print_and_increment()
c.print_and_increment()
print()
A = [counter()]*5
for c in A:
    c.print_and_increment()
print()
A = [counter() for i in range(5)]
for c in A:
    c.print_and_increment()
print()
A = [0]*5
for c in A:
    print(c)
    c = c+1
print()
    
def flipArray(A):
    B = [[] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[i])):
            #print(A[i][j])
            B[j].append(A[i][j])
    return B
A = [[1,2,3],[4,5,6],[7,8,9]]
B = flipArray(A)
print("Question 8")
print(A)
print(B)

def f(n, i=0):
    if n>0:
        i = f(n-1,i)
        i = f(n-1,i)
    print(i)
    return i+1
print()
print("Question 9")
f(1)

def flipArray2(A):
    return map(list, zip(*A))

A = [[1,2,3],[4,5,6],[7,8,9]]
flipArray2(A)
