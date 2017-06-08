import random

class HT():
    def __init__(self):
        self._T1 = [None] * 10#List of tuples
        self._T2 = [None] * 10#List of tuples
        self._r = random.random()

    def __getitem__(self,key):
        lst = self._T1
        b = hash((key,0,self._r)) % len(lst)

        while lst[b]:
            if lst[b][0] == key:
                return lst[b][1]
                #return lst[b]
            if lst == self._T1:
                lst = self._T2
                b = hash((key,1,self._r)) % len(lst)
            else:
                lst = self._T1
                b = hash((key,0,self._r)) % len(lst)
        #return (0,0)
        return None
        
    def __setitem__(self,k,v):
        lst = self._T1
        b = hash((k,0,self._r)) % len(lst)
        counter = 0
        
        if not lst[b]:
            lst[b] = (k,v)
            return

        while lst[b]:
            temp = lst[b]                
            lst[b] = (k,v)
            if temp[0] == k:
                return
            k,v = temp[0],temp[1]
            
            if lst == self._T1:
                lst = self._T2
                b = hash((k,1,self._r)) % len(lst)
            else:
                lst = self._T1
                b = hash((k,0,self._r)) % len(lst)

            counter += 1
            if counter >= 2*len(lst):
                temp1 = self._T1
                temp2 = self._T2
                self._T1 = [None] * (len(self._T1) * 2)
                self._T2 = [None] * (len(self._T2) * 2)
                self._r = random.random()
                for i in temp1:
                    if i:
                        #print(i)
                        self[i[0]] = i[1]
                for i in temp2:
                    if i:
                        #print(i)
                        self[i[0]] = i[1]

                counter = 0
                lst = self._T1
                b = hash((k,0,self._r)) % len(lst)
                #print("Infinite Loop")
            
        lst[b] = (k,v)

                
    def __delitem__(self,k):
        lst = self._T1
        b = hash((k,0,self._r)) % len(lst)
        while lst[b]:
            if lst[b][0] == k:
                lst[b] = None
                #return lst[b][1]
            if lst == self._T1:
                lst = self._T2
                b = hash((k,1,self._r)) % len(lst)
            else:
                lst = self._T1
                b = hash((k,0,self._r)) % len(lst)
        
    def __len__(self):
        counter = 0
        for i in self._T1:
            if i:
                counter += 1
        for i in self._T2:
            if i:
                counter += 1
        return counter
                
    def __contains__(self,key):
        for i in self._T1:
            if i and i[0] == key:
                return True
        for i in self._T2:
            if i and i[0] == key:
                return True

    def __iter__(self):
        for i in self._T1:
            if i:
                yield i
        for i in self._T2:
            if i:
                yield i

    def keys(self):
        for i in self._T1:
            if i:
                yield i[0]
        for i in self._T2:
            if i:
                yield i[0]
    def values(self):
        for i in self._T1:
            if i:
                yield i[1]
        for i in self._T2:
            if i:
                yield i[1]
    def items(self):
        for i in self._T1:
            if i:
                yield i
        for i in self._T2:
            if i:
                yield i

T = HT()
for i in range(200):
    T[i] = i*i
    #T[i] = T[i] + 1

for i in T.keys():
    #print(i)
    #print(T[i], T[i]+1)
    T[i] = T[i]+1
    #T[i] = T[i]

print()
for i in range(5,400):
    if i in T:
        del T[i]

K = list(T.items())
K.sort()
print(K)
print()
print(len(K))


