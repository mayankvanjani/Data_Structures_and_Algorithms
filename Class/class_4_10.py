class hashDict():
    def __init__(self):
        self._T = [[] for i in range(10)]

    def __setitem__(self,k,v):
        #bucket is num
        bucket = hash(k)%len(self._T)
        #self._T[bucket].append( (k,v) )
        #Only good for first setitem
        for i in range(len(self._T[bucket])):
            if self._T[bucket][i][0] == k:
                self._T[bucket][i] = (k,v)
                return
        self._T[bucket].append( (k,v) )
    
    def __getitem__(self,k):
        #bucket is list
        bucket = self._T[hash(k)%len(self._T)]
        for k2,v2 in bucket:
            if k == k2:
                return v2
        #KeyError here
        
    def __delitem__(self,k):
        bucket = self._T[hash(k)%len(self._T)]
        for i in range(len(bucket)):
            if k == bucket[i][0]:
                #popitem if u want to return value
                del bucket[i]
                return
        #KeyError here

    def __iter__(self):
        for i in self._T:
            for j in self._T[i]:
                yield j[0]
    #Same for yielding keys, values, items
            


        
