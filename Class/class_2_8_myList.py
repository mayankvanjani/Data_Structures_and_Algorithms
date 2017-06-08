import ctypes

class MyList():
    def __init__(self, I=None):
        self._A = self.make_array(1)
        self._cap = 1
        self._n = 0
        if not I: #I != None
            self.extend(I)
    def make_array(self,size):
        return (size*ctypes.py_object)()
    def append(self, x):
        if self._n == self._cap:
            newcap = self._cap + 1
            A = make_array(newcap)
            for i in range(self._n):
                A[i] = self._A[i]
            self._A = A
            self._cap = newcap
        self._A[self._n] = n
        self._n += 1
    '''
    def __getitem__(self, i):
        if i < 0:
            i = self._n + i
        return self._A[i]
    '''
    def __getitem__(self, i):
        if isinstance(i, slice):
            a = MyList()
            for j in range(*i.indices(self._n)):
                A.append(self[i])
            return A
        elif i < 0:
            i = self._n+i
        return self._A[i]
    def extend(self, I):
        for i in I:
            self.append(i)
    def len(self):
        return self._n
    def isempty(self):
        return len(self) == 0
    def __setitem__(self, i, x):
        if i < 0:
            i = self._n+i
        self._A[i] = x
    def __iter__(self):
        for i in range(len(self)):
            yield self[i]
    def __delitem__(self, i):
        for j in range(i, self._n-1):
            A[j] = A[j+1]
        self._n -= 1
        self[n] = None #Destroys last object pointer
    def pop(self, i=-1):
        r = self[i]
        del self[i]
        return r
    def __add__(self, B):#A+B add called on A with param B
        R = MyList(self)
        R.extend(B)
        return R
    def __mult__(self, i):#for A*1000
        R = MyList(self)
        for j in range(i): 
            #R = R+self
            R = R.extend(self)
        return R
    #def __rmult__(self, i):#for 1000*A OR
    __rmult__ = __mult__
    def __contains__(self, x):#in function
        for y in self:
            if x==y:
                return True
        return False
    def __str__(self):#O(n^2) time because keeps building new strings
        s = "["
        for x in self:
            s += str(x) + ","
        s += "]"
        return s

A = MyList(range(10,20,2))
print(A[2])
#i is set to 2 in getitem

B = A[1:3]#same as A[slice(1,3)] which is initializing slice class and getting an obj
#i is set to the slice 1:3
'''
isinstance True if var of type or False if nor
if isinstance in getitem now to differentiate slice vs num
also use indices function: i=s.indices(10) returns indices of range
i=s.indices(10) returns the range (1,3,1), 10 is size of list
now use for j in range(i[0],i[1],i[2]) or: use *
for j in range(*i)

del A[1:3] and A[0:5:2]=[1,2,3] also use splices
del removes [12,14] and the second => A=[1,12,2,16,3]
can also A[1:3]=[1,2,3,4] => A=[10,1,2,3,4,16,18]



'''

