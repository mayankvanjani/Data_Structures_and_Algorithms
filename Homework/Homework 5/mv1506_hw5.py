'''
Mayank Vanjani mv1506
Homework 5
2/28/17
'''

class LeakyStack():
    
    def __init__(self, maxsize):
        self._maxsize = maxsize
        self._lst = []
        self._len = 0

    def __len__(self):
        return self._len
    def is_empty(self):
        return self._len == 0
    
    def push(self, x):
        if self._len == self._maxsize:
            self._lst.append(x)
            self._lst[:1] = []
        else:
            self._lst += [x]
            self._len += 1

    def pop(self):
        if self._len == 0:
            return None
        x = self._lst[-1]
        self._lst[-1:] = []
        self._len -= 1
        return x

    def __str__(self):
        ans = "["
        for i in self._lst:
            if i==self._lst[-1]:
                ans += str(i)
            else:
                ans += str(i) + ","
        ans += "]"
        return ans

def main():
    A = LeakyStack(5)
    print("Values are added to the front of the stack(right) and leaked from the back(left)")
    print()
    
    print("LeakyStack of size 5 having values pushed to it:")
    print("\t     BACK\tFRONT")
    print("\t  A:", A)
    for i in range(0, 50, 5):
        A.push(i)
        if i < 10:
            print("Pushed", i, " A:", A)
        else:
            print("Pushed", i, "A:", A)
    print()
    
    print("Popping everything off:")
    print("\t   BACK\t\tFRONT")
    print("\tA:", A)
    while(A):
        A.pop()
        print("Popped, A:",A)

    print()
    print("Popping an empty LeakyStack:", A.pop())
    
main()
