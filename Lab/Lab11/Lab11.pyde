import random

class PQ():
    
    class _Node():
        def __init__(self,left,right,data):
            self._l = left
            self._r = right
            self._data = data
    
    def __init__(self, x=None):
        if isinstance(x, int):
            self._root = self._Node(None,None,x)
        elif x:
            self._root = x
        else:
            self._root = None
        
    def flip_help(self,curr):
        if curr:
            curr._l,curr._r = curr._r,curr._l
        
    def flip(self,curr="init"):
        if curr=="init":
            curr = self._root
            
        if curr:
            self.flip_help(curr)
            while curr._r:
                self.flip(curr._r)
                curr = curr._r
            '''
            if curr._l:
                self.flip(curr._l)
            if curr._r:
                self.flip(curr._r)
            '''
        
    def merge(self,h1,h2):
        ans = PQ()
        curr1 = h1._root
        curr2 = h2._root
        
        while curr1 or curr2:
            temp = ans._root
            while temp and temp._l:
                temp = temp._l
                
            #print(curr1._data,curr2._data)
            if (curr1 and not curr2):
                #print("Case 1")
                new_node = ans._Node(None,curr1._r,curr1._data)
                curr1 = curr1._l
            elif (curr2 and not curr1):
                #print("Case 2") 
                new_node = ans._Node(None,curr2._r,curr2._data)
                curr2 = curr2._l
            elif (curr1._data <= curr2._data):
                #print("Case 3")
                #print(curr1._r._data)
                new_node = ans._Node(None,curr1._r,curr1._data)
                curr1 = curr1._l
            elif (curr2._data < curr1._data):
                #print("Case 4")
                new_node = ans._Node(None,curr2._r,curr2._data)
                curr2 = curr2._l
                
            if temp:
                temp._l = new_node
                #temp._l = ans._Node(None,None,100)
            else:
                ans._root = new_node
        
        ans.flip()
        return ans
        
    def insert(self,x):
        #if self._root._l == None and self._root._r == None and self._root._data == None:
        #self._data = x
        if not self._root:
            self._root = self._Node(None,None,x)    
        else:
            temp = PQ(x)
            self._root = self.merge(self,temp)._root
            '''
            temp = PQ(x)
            pq = PQ()#self.merge(self,temp)
            pq._root = pq._Node(None,None,40)
            pq._root._r = pq._Node(None,None,25)
            self = pq
            '''
            
    def extractMin(self):
        #before = self
        if not self._root:
            return
        data = self._root._data
        #print(data)
        left = PQ(self._root._l)
        right = PQ(self._root._r)
        #self = self.merge(left,right)
        self._root = self.merge(left,right)._root
        #print(self == before)
        #if self._root:
        #print("Now:",self._root._data)
        #if before._root:
        #print("Before:",before._root._data)
        return data


#Just Call draw_tree on the root node and it will draw the tree
#Your node class must use ._l ._r and ._data

def subtree_size(node):
    if node is None:
      return 0
    else:
      return 1+subtree_size(node._l)+subtree_size(node._r)

def draw_tree(node,level=1,x=20,parx=None,pary=None):
    XSEP=5
    YSEP=5
    fill(0)
    textAlign(CENTER,CENTER)
    textSize(5)
    lsize=subtree_size(node._l)
    myx,myy=x+lsize*XSEP,YSEP*level
    text(str(node._data),myx,myy)
    if node._l is not None:
      draw_tree(node._l,level+1,x,myx,myy)
    if node._r is not None:
      draw_tree(node._r,level+1,x+(lsize+1)*XSEP,myx,myy)
    if parx is not None:
      strokeWeight(10)
      stroke(0,255,0,30)
      line(parx,pary,myx,myy)
      

print("Test")
A = list(range(20))
random.shuffle(A)
print(A)
pq = PQ()
for i in A:
    pq.insert(i)
print([pq.extractMin() for i in range(20)])

'''
print("Test2")
pq = PQ()
for i in range(20):
    pq.insert(i)
print("end")
draw_tree(pq._root)
'''
'''
pq = PQ()
pq2 = PQ()
pq._root = pq._Node(None,None,40)
pq._root._r = pq._Node(None,None,25)
pq2._root = pq._Node(None,None,200)
x = pq.merge(pq,pq2)

while x._root:
    print(x._root)
    print(x.extractMin())
print("Test")
draw_tree(x._root)
'''