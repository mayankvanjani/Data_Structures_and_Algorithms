Suppose you work for an airline. Your task is to write a program to help them automate the task of figuring out who to remove from a flight after you have boarded too many people. You have passenger records with the following information:
 
First name
Last name
Status (one of the strings "None" "Gold" "Silver" "Platinum" "1K" "Global Services", "Employee")
Fare Paid
Number of checked bags
 
These are stored in a Passenger class, which has a constructor which must work in the obvious way:
 
john=Passenger("John","Iacono","Platinum",532,1)
 
Your task is to create a Flight class, which should have methods that work as follows:
 
UA3411=Flight(101) #Constructor which takes the capacity of the flight

UA3411.board(john) #Puts this passenger on the flight

UA3411.finalize() #After this is called, further calls to board are prohibited

dragList=UA3411.whoToRemove() #Returns a list of the passengers who should be removed. Finalize must be called before calling this method
 
WhoToRemove removes passengers as needed to reduce the number to the the capacity of the flight. If the capacity is not reached, no one is removed. However, if people need to be removed, this is done according to their status (None is the lowest and employee is the highest). However, if there is a tie in status, this is done according to whether or not they checked bags (people who checked at least 1 bag should not be deplaned if possible). If there remains a tie, the fare paid, with the higher fares given preference to stay on the plane (of course!). If there is a tie in the status, bag check status, and fare paid, deplaning is done according to the order of boarding (last to board should be kicked off).
 
Read §9.3.7, you must use Python's heapq module to store the Passengers in the Flight class. You must develop tests that demonstrate that your code works, and tests all possible situations (e.g. all possible ties).
 
Your code must run init and board in time O(1), finalize in time O(n), where n is the number of board operations, and whoToRemove in time O(dlogn) where d is the number of passengers removed from the plane.
 
Hint: You will need to code things like __le__ to get this to work. You can add private methods, classes, and fields as needed.
