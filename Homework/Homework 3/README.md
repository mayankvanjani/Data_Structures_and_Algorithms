Homework 3

Your task this week is to code a class aList, which supports the following methods. Some work the same as the python List class, some do not.
 
You can and should start with the book's code for the class it calls DynamicArray. Download it (and all of the book's code while you are at it) from the books's web page. Do not use python's List class.
 
aList(), aList(I), A.append(x), len(A), is_empty, str(A), iter(A) should all work like in a python list, where A represents an aList.
 
A[i], A[i]=x, del A[i] should work like in a Python list, except if i is bigger than or equal to len(A) you want it to wrap around rather than giving an error. I.e., if the aList A has 10 items, A[522] should return the same thing as A[2]. Use mod, % in Python.
 
Suppose A=aList([1,2,3]) and B=aList([4,5,6]). Have A+B return the new aList [5,7,9] (adding the two lists, NOT concatenating them like in python). This should happen if A or B is a aList and the other is anything iterable. If one list is shorter than the other, treat the missing elements of the shorted list as 0's. Code -, += and -= also. Keep in mind += and -= should change the list to the left of the operator, whereas + and - do not change the given lists, they return a new list. 
 
Suppose A=aList[1,2,3]. have A*i return a new list where every element of A is repeated i times. For example, if A=[1,2,3], A*i should return a new list with [1,1,1,2,2,2,3,3]. Code *= also. A*=3 will change A. 
 
Suppose A=aList[1,2,3]. have i*A return a new list where every element of A is multiplied by i. For example, if A=[1,2,3], i*A should return a new list with [3,6,9]. 
 
Code a method revitr which allows you to iterate though the elements in reverse order. Suppose A=aList[1,2,3]. Then B=aList(A.revitr()) should set B to [3,2,1].
 
A.select(I). Creates a new aList based on the given indicies. An example: Suppose A=aList([10,4,2,1,15,23,23]). If we run A.select([0,2,4]) this would return a new aList containing [A[0],A[2],A[4]] = [10,2,15]. You should be able to pass any iterable with the indicies to select, for example a range (A.select(range(0,6,2)) should be the same as the above), a aList or a python List.
