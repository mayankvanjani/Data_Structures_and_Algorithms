This assignment concerns the code in @110 for BSTs, and BST's in general. Feel free to add default parameters and helper methods as needed.
 
1. Code __iter__ that will return everything in the tree in order.
 
2. Code T.search_ge(x) that will return the smallest item in the tree ≥ x.
 
3. Make len(T) work in O(1) time.
 
4. Code T.print() that will print out an an ASCII version of the tree that looks like this:
 
        50        
      40    70    
  20      60    90
10  30        80  
Here the tree has a root of 50, and its children are 40 and 70, which are on the next line and are to the left and right of 50. This diagram has the hollowing features:
For any node, its children should be printed on the next line.
The items appear in order from left to right
Exactly one item is printed in each column
No more rows than are needed are printed. (No blank lines).
 
5. Add a position inner class to the tree, which has a public method p.element(). Code p=T.first() and p=T.last() which returns positions to the smallest and largest items in the BST, and p'=T.before(p) and p'=T.after(p) that given a position returns a position to the item before or after in the BST in sorted order.
 
6. Code T.pos_ge(x) and T.pos_le(x) that do the same thing as search_ge and search_le except they return a position rather than a value.
 
7. Code T.range(x,y) T.pos_range(x,y) which returns an iterator which returns the data in the tree that is at least x and less than y. T.range will return an iterator to the values, and pos_range will return an iterator to the position.
 
8. Show how to build the following balanced tree (printed by your print function) through insertion:
 
                                                     32                                                              
                     16                                                              48                              
       8                             24                              40                              56              
   4         12              20              28              36              44              52              60      
 2   6   10      14      18      22      26      30      34      38      42      46      50      54      58      62  
1 3 5 7 9  11  13  15  17  19  21  23  25  27  29  31  33  35  37  39  41  43  45  47  49  51  53  55  57  59  61  63
You should do this programmatically and not by writing 63 insertion statements!
 
9. Show how to build the following tree (printed by your print function) though insertion:
 
0                             
                            20
 1                            
                          19  
  2                           
                        18    
   3                          
                      17      
    4                         
                    16        
     5                        
                  15          
      6                       
                14            
       7                      
              13              
        8                     
            12                
         9                    
          11 
