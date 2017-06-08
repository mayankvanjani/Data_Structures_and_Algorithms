'''
Mayank Vanjani mv1506
Homework 7
3/28/17
'''

#Copied Tree, BinaryTree, and LinkedBinaryTree Code from Textbook#

#from linked_queue import LinkedQueue
import collections

class Tree:
  """Abstract base class representing a tree structure."""
  #------------------------------- nested Position class -------------------------------
  class Position:
    """An abstraction representing the location of a single element within a tree.

    Note that two position instaces may represent the same inherent location in a tree.
    Therefore, users should always rely on syntax 'p == q' rather than 'p is q' when testing
    equivalence of positions.
    """

    def element(self):
      """Return the element stored at this Position."""
      raise NotImplementedError('must be implemented by subclass')
      
    def __eq__(self, other):
      """Return True if other Position represents the same location."""
      raise NotImplementedError('must be implemented by subclass')

    def __ne__(self, other):
      """Return True if other does not represent the same location."""
      return not (self == other)            # opposite of __eq__

  # ---------- abstract methods that concrete subclass must support ----------
  def root(self):
    """Return Position representing the tree's root (or None if empty)."""
    raise NotImplementedError('must be implemented by subclass')

  def parent(self, p):
    """Return Position representing p's parent (or None if p is root)."""
    raise NotImplementedError('must be implemented by subclass')

  def num_children(self, p):
    """Return the number of children that Position p has."""
    raise NotImplementedError('must be implemented by subclass')

  def children(self, p):
    """Generate an iteration of Positions representing p's children."""
    raise NotImplementedError('must be implemented by subclass')

  def __len__(self):
    """Return the total number of elements in the tree."""
    raise NotImplementedError('must be implemented by subclass')

  # ---------- concrete methods implemented in this class ----------
  def is_root(self, p):
    """Return True if Position p represents the root of the tree."""
    return self.root() == p

  def is_leaf(self, p):
    """Return True if Position p does not have any children."""
    return self.num_children(p) == 0

  def is_empty(self):
    """Return True if the tree is empty."""
    return len(self) == 0

  def depth(self, p):
    """Return the number of levels separating Position p from the root."""
    if self.is_root(p):
      return 0
    else:
      return 1 + self.depth(self.parent(p))

  def _height1(self):                 # works, but O(n^2) worst-case time
    """Return the height of the tree."""
    return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

  def _height2(self, p):                  # time is linear in size of subtree
    """Return the height of the subtree rooted at Position p."""
    if self.is_leaf(p):
      return 0
    else:
      return 1 + max(self._height2(c) for c in self.children(p))

  def height(self, p=None):
    """Return the height of the subtree rooted at Position p.

    If p is None, return the height of the entire tree.
    """
    if p is None:
      p = self.root()
    return self._height2(p)        # start _height2 recursion

  def __iter__(self):
    """Generate an iteration of the tree's elements."""
    for p in self.positions():                        # use same order as positions()
      yield p.element()                               # but yield each element

  def positions(self):
    """Generate an iteration of the tree's positions."""
    return self.preorder()                            # return entire preorder iteration

  def preorder(self):
    """Generate a preorder iteration of positions in the tree."""
    if not self.is_empty():
      for p in self._subtree_preorder(self.root()):  # start recursion
        yield p

  def _subtree_preorder(self, p):
    """Generate a preorder iteration of positions in subtree rooted at p."""
    yield p                                           # visit p before its subtrees
    for c in self.children(p):                        # for each child c
      for other in self._subtree_preorder(c):         # do preorder of c's subtree
        yield other                                   # yielding each to our caller

  def postorder(self):
    """Generate a postorder iteration of positions in the tree."""
    if not self.is_empty():
      for p in self._subtree_postorder(self.root()):  # start recursion
        yield p

  def _subtree_postorder(self, p):
    """Generate a postorder iteration of positions in subtree rooted at p."""
    for c in self.children(p):                        # for each child c
      for other in self._subtree_postorder(c):        # do postorder of c's subtree
        yield other                                   # yielding each to our caller
    yield p                                           # visit p after its subtrees

  def breadthfirst(self):
    """Generate a breadth-first iteration of the positions of the tree."""
    if not self.is_empty():
      fringe = LinkedQueue()             # known positions not yet yielded
      fringe.enqueue(self.root())        # starting with the root
      while not fringe.is_empty():
        p = fringe.dequeue()             # remove from front of the queue
        yield p                          # report this position
        for c in self.children(p):
          fringe.enqueue(c)              # add children to back of queue

class BinaryTree(Tree):
  """Abstract base class representing a binary tree structure."""

  # --------------------- additional abstract methods ---------------------
  def left(self, p):
    """Return a Position representing p's left child.

    Return None if p does not have a left child.
    """
    raise NotImplementedError('must be implemented by subclass')

  def right(self, p):
    """Return a Position representing p's right child.

    Return None if p does not have a right child.
    """
    raise NotImplementedError('must be implemented by subclass')

  # ---------- concrete methods implemented in this class ----------
  def sibling(self, p):
    """Return a Position representing p's sibling (or None if no sibling)."""
    parent = self.parent(p)
    if parent is None:                    # p must be the root
      return None                         # root has no sibling
    else:
      if p == self.left(parent):
        return self.right(parent)         # possibly None
      else:
        return self.left(parent)          # possibly None

  def children(self, p):
    """Generate an iteration of Positions representing p's children."""
    if self.left(p) is not None:
      yield self.left(p)
    if self.right(p) is not None:
      yield self.right(p)

  def inorder(self):
    """Generate an inorder iteration of positions in the tree."""
    if not self.is_empty():
      for p in self._subtree_inorder(self.root()):
        yield p

  def _subtree_inorder(self, p):
    """Generate an inorder iteration of positions in subtree rooted at p."""
    if self.left(p) is not None:          # if left child exists, traverse its subtree
      for other in self._subtree_inorder(self.left(p)):
        yield other
    yield p                               # visit p between its subtrees
    if self.right(p) is not None:         # if right child exists, traverse its subtree
      for other in self._subtree_inorder(self.right(p)):
        yield other

  # override inherited version to make inorder the default
  def positions(self):
    """Generate an iteration of the tree's positions."""
    return self.inorder()                 # make inorder the default



###MODIFICATIONS TO THIS CLASS###
class LinkedBinaryTree(BinaryTree):
  """Linked representation of a binary tree structure."""

  #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a node."""
    __slots__ = '_element', '_parent', '_left', '_right' # streamline memory usage

    def __init__(self, element, parent=None, left=None, right=None):
      self._element = element
      self._parent = parent
      self._left = left
      self._right = right

  #-------------------------- nested Position class --------------------------
  class Position(BinaryTree.Position):
    """An abstraction representing the location of a single element."""

    def __init__(self, container, node):
      """Constructor should not be invoked by user."""
      self._container = container
      self._node = node

    def element(self):
      """Return the element stored at this Position."""
      return self._node._element

    def __eq__(self, other):
      """Return True if other is a Position representing the same location."""
      return type(other) is type(self) and other._node is self._node

  #------------------------------- utility methods -------------------------------
  def _validate(self, p):
    """Return associated node, if position is valid."""
    if not isinstance(p, self.Position):
      raise TypeError('p must be proper Position type')
    if p._container is not self:
      raise ValueError('p does not belong to this container')
    if p._node._parent is p._node:      # convention for deprecated nodes
      raise ValueError('p is no longer valid')
    return p._node

  def _make_position(self, node):
    """Return Position instance for given node (or None if no node)."""
    return self.Position(self, node) if node is not None else None

  #-------------------------- binary tree constructor --------------------------
  def __init__(self):
    """Create an initially empty binary tree."""
    self._root = None
    self._size = 0

  #-------------------------- public accessors --------------------------
  def __len__(self):
    """Return the total number of elements in the tree."""
    return self._size
  
  def root(self):
    """Return the root Position of the tree (or None if tree is empty)."""
    return self._make_position(self._root)

  def parent(self, p):
    """Return the Position of p's parent (or None if p is root)."""
    node = self._validate(p)
    return self._make_position(node._parent)

  def left(self, p):
    """Return the Position of p's left child (or None if no left child)."""
    node = self._validate(p)
    return self._make_position(node._left)

  def right(self, p):
    """Return the Position of p's right child (or None if no right child)."""
    node = self._validate(p)
    return self._make_position(node._right)

  def num_children(self, p):
    """Return the number of children of Position p."""
    node = self._validate(p)
    count = 0
    if node._left is not None:     # left child exists
      count += 1
    if node._right is not None:    # right child exists
      count += 1
    return count

  #-------------------------- nonpublic mutators --------------------------
  def _add_root(self, e):
    """Place element e at the root of an empty tree and return new Position.

    Raise ValueError if tree nonempty.
    """
    if self._root is not None:
      raise ValueError('Root exists')
    self._size = 1
    self._root = self._Node(e)
    return self._make_position(self._root)

  def _add_left(self, p, e):
    """Create a new left child for Position p, storing element e.

    Return the Position of new node.
    Raise ValueError if Position p is invalid or p already has a left child.
    """
    node = self._validate(p)
    if node._left is not None:
      raise ValueError('Left child exists')
    self._size += 1
    node._left = self._Node(e, node)                  # node is its parent
    return self._make_position(node._left)

  def _add_right(self, p, e):
    """Create a new right child for Position p, storing element e.

    Return the Position of new node.
    Raise ValueError if Position p is invalid or p already has a right child.
    """
    node = self._validate(p)
    if node._right is not None:
      raise ValueError('Right child exists')
    self._size += 1
    node._right = self._Node(e, node)                 # node is its parent
    return self._make_position(node._right)

  def _replace(self, p, e):
    """Replace the element at position p with e, and return old element."""
    node = self._validate(p)
    old = node._element
    node._element = e
    return old

  def _delete(self, p):
    """Delete the node at Position p, and replace it with its child, if any.

    Return the element that had been stored at Position p.
    Raise ValueError if Position p is invalid or p has two children.
    """
    node = self._validate(p)
    if self.num_children(p) == 2:
      raise ValueError('Position has two children')
    child = node._left if node._left else node._right  # might be None
    if child is not None:
      child._parent = node._parent   # child's grandparent becomes parent
    if node is self._root:
      self._root = child             # child becomes root
    else:
      parent = node._parent
      if node is parent._left:
        parent._left = child
      else:
        parent._right = child
    self._size -= 1
    node._parent = node              # convention for deprecated node
    return node._element
  
  def _attach(self, p, t1, t2):
    """Attach trees t1 and t2, respectively, as the left and right subtrees of the external Position p.

    As a side effect, set t1 and t2 to empty.
    Raise TypeError if trees t1 and t2 do not match type of this tree.
    Raise ValueError if Position p is invalid or not external.
    """
    node = self._validate(p)
    if not self.is_leaf(p):
      raise ValueError('position must be leaf')
    if not type(self) is type(t1) is type(t2):    # all 3 trees must be same type
      raise TypeError('Tree types must match')
    self._size += len(t1) + len(t2)
    if not t1.is_empty():         # attached t1 as left subtree of node
      t1._root._parent = node
      node._left = t1._root
      t1._root = None             # set t1 instance to empty
      t1._size = 0
    if not t2.is_empty():         # attached t2 as right subtree of node
      t2._root._parent = node
      node._right = t2._root
      t2._root = None             # set t2 instance to empty
      t2._size = 0

  ###Question 1###      
  def max(self, temp=None, pos=None):
    if temp == None and pos == None:
      pos = self.root()
      temp = pos.element()
      
    if self.is_leaf(pos):
      #print("original", temp, "now", pos.element())
      return max(pos.element(), temp)
    if self.left(pos):
      temp =  max(temp, self.max(temp,self.left(pos)))
    if pos:
      #print("original", temp, "now", pos.element())
      temp = max(temp, pos.element())
    if self.right(pos):
      temp =  max(temp, self.max(temp,self.right(pos)))

    return temp
  
  ###Question 2###      
  def leaves_list(self, temp=None, pos=None):
    if temp==None and pos==None:
      temp = []
      pos = self.root()
      
    if self.is_leaf(pos):
      #print(pos.element())
      temp.append(pos.element())
    
    if self.left(pos):
      ( self.leaves_list(temp,self.left(pos)) )
    if self.right(pos):
      ( self.leaves_list(temp,self.right(pos)) )
    return temp

  ###Question 3###
  def is_height_balanced(self, pos="init"):
    if pos=="init":
      pos = self.root()

    result = self._height_helper(pos)
    if result > 0:
      return True
    else:
      return False
    
  def _height_helper(self,pos):
    if pos == None:
      return 0
    lefth = self._height_helper(self.left(pos))
    if lefth == -1:
      return -1
    righth = self._height_helper(self.right(pos))
    if righth == -1:
      return -1
    if lefth-righth > 1 or righth-lefth > 1:
      return -1
    return 1 + max(lefth,righth)    
    
  ###Question 4###
  def iterative_inorder(self):
    curr = self.root()
    l_done = False

    while curr:
      if not l_done:
        while self.left(curr):
          curr = self.left(curr)

      yield curr.element()
      l_done = True
      
      if self.right(curr):
        l_done = False
        curr = self.right(curr)
      elif self.parent(curr):
        while self.parent(curr) and curr == self.right(self.parent(curr)):
          curr = self.parent(curr)
        if not self.parent(curr):
          break
        curr = self.parent(curr)
      else:
        break

  def number_at_depth(self,d,curr="init"):
    if curr=="init":
      curr = self._root
    if not curr:
      return 0
    if d == 0:
      return 1
    left = self.number_at_depth(d-1,curr._left)
    right = self.number_at_depth(d-1,curr._right)
    return left+right
###Other Methods: Question 5###

#a#
def create_expression_tree(prefix_exp_str):
  elem_lst = prefix_exp_str.split(" ")
  T,dummy = create_expression_tree_helper(elem_lst)
  return T
  
def create_expression_tree_helper(prefix_exp, start_pos=0):
  op = "+-*/"
  element = prefix_exp[start_pos]
  #print("elem:",element)
  #print("pos:",start_pos)
  if element in op:
    start_pos += 1
    left_t,left_s = create_expression_tree_helper(prefix_exp, start_pos)
    start_pos += left_s
    right_t,right_s = create_expression_tree_helper(prefix_exp, start_pos)

    T = LinkedBinaryTree()
    T._add_root(element)
    T._attach(T.root(), left_t, right_t)
    return (T,left_s+right_s+1)

  else:
    T = LinkedBinaryTree()
    T._add_root(int(element))
    return (T,1)

#b#
#since helper modifies a list, we need to unnest the list and join
def unnest(A, ans=None):
  if ans == None:
    ans = []
  for i in A:
    if isinstance(i, list):
      ans += unnest(i)
    else:
      ans += [i]
  return ans

def prefix_to_postfix(prefix_exp_str):
  elem_lst = prefix_exp_str.split(" ")
  T,dummy = create_expression_tree_helper(elem_lst)
  lst = unnest(prefix_to_postfix_helper(T))
  print(" ".join(lst))

def prefix_to_postfix_helper(tree,curr="init"):
  ans = [] #faster to append to list than add strings
  if curr == "init":
    curr = tree.root()
  if tree.left(curr):
    ans.append( prefix_to_postfix_helper(tree,tree.left(curr)))
  if tree.right(curr):
    ans.append( prefix_to_postfix_helper(tree,tree.right(curr))) 
  ans.append(str(curr.element()))
  return ans #list of strings in post order
  
'''
###Testing Tree Methods###
# Max, Leaves_List, Height_Balanced, and Iterative_Inorder #
print("FIRST Test Tree of Question 3")
T = LinkedBinaryTree()
T._add_root(3)
T._add_left(T.root(),2)
left = T.left(T.root())
T._add_left(left,9)
T._add_right(T.root(),7)
right = T.right(T.root())
T._add_left(right,8)
T._add_right(right,4)
left = T.left(right)
T._add_left(left,5)
T._add_right(left,1)
for i in T:
  print(i)
print("MAX:", T.max())
print("LEAVES: ", T.leaves_list())
print("Height Balanced? ", T.is_height_balanced())
print("Iterative Inorder:", end="  ")
for item in T.iterative_inorder():
  print(item,end=" ")
print("\n")

print("SECOND Test Tree of Question 3")
T2 = LinkedBinaryTree()
T2._add_root(3)
T2._add_left(T2.root(),2)
left = T2.left(T2.root())
T2._add_left(left,9)
left = T2.left(left)
T2._add_left(left,5)
T2._add_right(left,1)
T2._add_right(T2.root(),7)
right = T2.right(T2.root())
T2._add_left(right,8)
T2._add_right(right,4)
for i in T2:
  print(i)
print("MAX:", T2.max())
print("LEAVES: ", T2.leaves_list())
print("Height Balanced? ", T2.is_height_balanced())
print("Iterative Inorder:", end="  ")
for item in T2.iterative_inorder():
  print(item,end=" ")
print("\n\n")

###Testing Question 5###
print("Testing Question 5 Prefix Expressions")
x = ('* 2 + - 15 6 4')
print("Prefix Expression:", x)
prefix_T = create_expression_tree(x)
print("Iterative Inorder:", end="  ")
for item in prefix_T.iterative_inorder():
  print(item,end=" ")
print()
print("Prefix => Postfix:")
prefix_to_postfix(x)
print("\n")

y = ('* 3 25')
print("Prefix Expression:", y)
prefix_T = create_expression_tree(y)
print("Iterative Inorder:", end="  ")
for item in prefix_T.iterative_inorder():
  print(item,end=" ")
print()
print("Prefix => Postfix:")
prefix_to_postfix(y)
print("\n")
'''

T = LinkedBinaryTree()
T._add_root(3)
print("H:",T.height())
T._add_left(T.root(),2)
print("H:",T.height())
left = T.left(T.root())
T._add_left(left,9)
T._add_right(T.root(),7)
right = T.right(T.root())
T._add_left(right,8)
T._add_right(right,4)
left = T.left(right)
T._add_left(left,5)
T._add_right(left,1)
for i in T:
  print(i)
print()
print(T.number_at_depth(3))
print()


#print(T2.height())

