'''
Mayank Vanjani mv1506
Homework 11
4/23/17
'''

import heapq

counter = 1

class Passenger():

    def __init__(self,first,last,status,fare,bags):
        self._first = first
        self._last = last
        self._status = status
        self._fare = fare
        self._bags = bags
        global counter
        self._counter = counter
        counter += 1
        
    def __str__(self):
        return ("" + self._first + " " + self._last + ":" +
                "\tStatus:"+self._status +
                "  Fare: $"+str(self._fare) +
                "  Bags:"+str(self._bags) +
                "  Boarding Number:"+str(self._counter) )

    def __lt__(self, P):
        status = {"None":0,"Gold":1,"Silver":2,"Platinum":3,
                  "1K":4,"Global Services":5,"Employee":6}

        if status[self._status] < status[P._status]: #status check
            return True
        elif status[self._status] > status[P._status]:
            return False
        else: # ==
            
            #if self._bags < P._bags: #less bags
            if self._bags == 0 and self._bags < P._bags:
                return True
            elif P._bags == 0 and self._bags > P._bags:
                return False
            else:
                
                if self._fare < P._fare: #payed less
                    return True
                elif self._fare > P._fare:
                    return False
                else:
                    
                    if self._counter > P._counter: #boarded later
                        return True
                    else:
                        return False

                    
class Flight():
                                             
    def __init__(self,capacity):
        self._capacity = capacity
        self._lst = []
        self._final = False

    def __str__(self):
        print("\nFLIGHT:")
        ans = ''
        if len(self._lst) == 0:
            ans += "Flight Empty"
        for people in self._lst:
            ans += str(people) + "\n"
        return ans
            
    def board(self,passenger):
        if not isinstance(passenger,Passenger):
            print("Unable To Board")
        elif not self._final:
            self._lst.append(passenger)
        else:
            print("Cannot Add A Passenger, Flight is Finalized")

    def finalize(self):
        if not self._final:
            self._final = True
            print("Finalized Passenger List: Capacity", self._capacity)
            for passenger in self._lst:
                print (passenger)
            heapq.heapify(self._lst)
        else:
            print("Already Finalized")

    def whoToRemove(self):
        removed = []
        if not self._final:
            print("Cannot Remove Without Finalizing the Flight")
            return
        else:
            #print(len(self._lst) - self._capacity)
            for i in range(len(self._lst) - self._capacity):
                temp = heapq.heappop(self._lst)
                removed.append(temp)
                #print(temp)
        if len(removed) == 0:
            print("Nobody Removed, Space for Everyone")
        return removed


'''
john = Passenger("John","Iacono","None",531,2)
jim = Passenger("Jim","Jim","None",531,2)
print(john)
print(jim)
print ("Jim <= John?: ",jim <= john)
'''
nemo = Passenger("Capt","Nemo","Employee",0,0)
john=Passenger("John","Iacono","Platinum",532,1)
jim = Passenger("Jim","Jim","Platinum",500,0)
josh = Passenger("Josh","Josh","None",100,0)
jacob = Passenger("Attdt.","Jacob","Employee",0,3)
Max = Passenger("Max","Pegasus","Platinum",501,0)
Fred = Passenger("Fred","Weasley","Gold",500,10)
George = Passenger("George","Weasley","Gold",500,9)
Harry = Passenger("Harry","Potter","None",100,1)
print()
people = [nemo,john,jim,josh,jacob,Max,Fred,George,Harry]


print("###Flight UA3411###")
UA3411 = Flight(0)
for i in people:
    UA3411.board(i)


print("Calling whoToRemove() before Finalize:")
dragList = UA3411.whoToRemove()
print()
UA3411.finalize()
print()

print("Tring to board after Finalized:")
late = Passenger("Doctor","Doctor","Silver",150,2)
UA3411.board(late)
print()
print("Removing Excess People")
dragList = UA3411.whoToRemove()
for excess in dragList:
    print(excess)
print(UA3411)


print("\n\n")

print("###Flight UA3412###")
UA3412 = Flight(5)
for i in people:
    UA3412.board(i)
    
UA3412.finalize()
print()
print("Removing Excess People")
dragList = UA3412.whoToRemove()
for excess in dragList:
    print(excess)
print(UA3412)
print()


print("\n\n")

print("###Flight UA3413###")
UA3413 = Flight(10)
for i in people:
    UA3413.board(i)
    
UA3413.finalize()
print()
print("Removing Excess People")
dragList = UA3413.whoToRemove()
for excess in dragList:
    print(excess)
print(UA3413)
