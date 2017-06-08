Consider the following code:

C=Counters()           
D=Counters()
cc=C.new_counter("A counter in C")
D.increment_counter(cc)
This should not work, since you are giving D a counter from C. It does not work. It gives the following error:

ValueError: p does not belong to this PList
This error comes from within the PList class, and thus may be confusing to users of the Counters class, who may have no idea there is a PList or what this error means. Your task is to change the code of the Counters class so that you receive the following error instead:

ValueError: counter does not belong to this Counter

You can only change the code of Counters. You can not change Plist.
 
2. In Counters, init, new_counter and delete_counter run in O(1) time. However, increment_counter could run in O(N) time if there are many ties.
 
Your task is to make increment_counter run in O(1) time. In the implementation I gave you, increment_counter is slow when the linked list contains many elements with the same count. You are to fix this by having all the items with the same count stored in one linked list node. Thus, the data in a linked list node may have several things and you need a data structure for this. Which one should you use? Use a linked list! Thus your data structure will be a linked list of linked lists! You will need to make substantial changes in the code to get this to work.
 
You can only change the code of Counters. You can not change Plist.
 
Counters should have exactly the same functionality as before, but will be faster. You can not have any loops in your code other than in __iter__.
 
The following picture illustrates what your data structure should look like. Note positions are not illustrated, and a big part of what you have to do is to figure out how to make them work.
 
 

 
3. Write code that uses the old and new versions of Counters that demonstrates the speedup. It should do exactly the same thing on both but runs noticeably faster on your improved version of Counters.
