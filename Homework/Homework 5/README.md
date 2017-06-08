You should make a class LeakyStack. It should support __init__(self,maxsize), push(self,x), pop(self), __len__(self), is_empty(self) and __str__(self).
 
The constructor takes a parameter which specifies the maximum number of items the stack can hold. If the stack reaches this size, and a push is performed, the oldest item in the stack is removed and forgotten. __str__ is for debugging, code something reasonable.
 
Write some code that demonstrates your stack and its leaky features.
 
Important:
For instance variables you may use a python list, and integers. Nothing else. Nothing. No credit if you violate this rule.
All operations except __str__ should run in constant time (assuming append on lists takes constant time).
