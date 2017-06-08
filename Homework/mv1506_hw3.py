'''                                                                                               
Mayank Vanjani mv1506
Homework 3
2/16/17
'''

import ctypes

class aList():
    def __init__(self, I=None):
        self._n = 0 #Number of elements
        self._cap = 1 #Capacity
        self._A = self._make_array(self._cap)
        if I:
            self.extend(I)

    def _make_array(self, c):
        return (c*ctypes.py_object)()
    
    def __len__(self):
        return self._n
    def is_empty(self):
        return self._n == 0

    def _resize(self, c):#For append although not necessary
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._cap = c
        
    def append(self, x):
        if self._n == self._cap:
            self._resize(2*self._cap)
        self._A[self._n] = x
        self._n += 1
    def extend(self, i):
        for x in i:
            self.append(x)
            
    def __iter__(self):
        for i in range(self._n):
            yield self._A[i]

    def __getitem__(self,i):
        if isinstance(i, slice):
            A=aList()
            for j in range(*i.indices(self._n)):
                A.append(self._A[j])
            return A
        i = i%self._n
        if i < 0:
            i = self._n+i
        return self._A[i]
    
    def __setitem__(self, i, x):        
        i = i%self._n
        if i < 0:
            i = self._n + i
        self._A[i] = x

    def __delitem__(self,i, check=None):
        if isinstance(i,slice):
            A=aList()
            for j in (range(*i.indices(self._n))):
                j = j%self._n
                if j < 0:
                    j = self._n + j
                A.append(self[:j])
                if check==None:
                    del self[j]
                    check=1
                else:
                    del self[j-check]
                    check+=1
        else:
            i = i%self._n
            if i < 0:
                i = self._n + i
            for j in range(i, self._n-1):
                self._A[j] = self._A[j+1]
            self[-1] = None
            self._n -= 1
            
    def __str__(self):
        return "[" + \
            "".join( str(i)+"," for i in self[:-1]) + \
            (str(self[-1]) if not self.is_empty() else "") + \
            "]"

    #+, -, +=, -= OPERATIONS
    def __add__(self, B):
        R = aList(self)
        if len(R) >= len(B):
            for i in range(len(B)):
                R[i] = R[i]+B[i]
        else:
            for i in range(len(B)):
                if i >= len(R):
                    R.append(B[i])
                else:
                    R[i] = R[i] + B[i]
        return R
    def __sub__(self, B):
        R = aList(self)
        if len(R) >= len(B):
            for i in range(len(B)):
                R[i] = R[i]-B[i]
        else:
            for i in range(len(B)):
                if i >= len(R):
                    R.append(-1 * B[i])
                else:
                    R[i] = R[i] - B[i]
        return R

    def __iadd__(self, B):
        if len(self) >= len(B):
            for i in range(len(B)):
                self._A[i] = self._A[i]+B[i]
        else:
            for i in range(len(B)):
                if i >= len(self):
                    self.append(B[i])
                else:
                    self._A[i] = self._A[i] + B[i]
        return(self)
    def __isub__(self, B):
        if len(self) >= len(B):
            for i in range(len(B)):
                self._A[i] = self._A[i]-B[i]
        else:
            for i in range(len(B)):
                if i >= len(self):
                    self.append(-1 * B[i])
                else:
                    self._A[i] = self._A[i] - B[i]
        return(self)

    #Special Multiplication
    def __mul__(self, i):
        R = aList()
        for j in range(self._n):
            for k in range(i):
                R.append(self._A[j])
        return R
    def __rmul__(self, i):
        for j in range(self._n):
            self._A[j] = self._A[j]*i
        return self

    #Reverse aList
    def _revitr(self):
        B = aList(self)
        for i in range(len(B)//2):
            B[i],B[len(B)-i-1]=B[len(B)-i-1],B[i]
        return B

    #Selection from an aList
    def select(self, i):
        R = aList()
        for j in i:
            R.append(self._A[j])
        return R
        
def main():
    A = aList([1,2,3,4,5])
    B = (1,2,3)
    print("A:", A)
    print()
    
    del A[0]
    print("Deleting A[0]")
    print("A:", A)
    del A[0:2]
    print("Deleting A[0:2]")
    print()
    
    print("A:", A)
    print("B:", B)
    print("A+B:", A+B)
    print("A-B:", A-B)
    A+=B
    print("A+=B => A =", A)
    A-=B
    print("A-=B => A =", A)
    print("A*3:", A*3)
    #print("B*4:", B*4)
    print("4*A:", 4*A)
    #print("3*B:", 3*B)
    print()
    
    A = aList([1,2,3])
    B = aList(A._revitr())
    print("A:", A, "\tAfter revitr:", B)
    print()
    
    A=aList([10,4,2,1,15,23,23])
    select = [0,2,4]
    x = A.select([0,2,4])
    print("A =", A)
    print("Selecting", select, "in A")
    print(x)

main()
