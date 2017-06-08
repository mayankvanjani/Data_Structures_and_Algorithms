import random

def select(lst, num):
    #print(lst)
    seperated = sep(lst)
    #print(seperated)
    group_sort(seperated)
    #print(seperated)
    if len(seperated) == 1:
        return seperated[0][num]
    median = []
    for i in seperated:
        if len(i) >= 3:
            median.append(i[2])
        else:
            median.append(i[-1])
    #print("Median:",median)
    MidofMid = select(median,len(median)//2)
    #MidofMid = MoM(median)
    #print(MidofMid)
    less = []
    equal = []
    more = []
    for i in lst:
        if i < MidofMid:
            less.append(i)
        elif i > MidofMid:
            more.append(i)
        else:
            equal.append(i)

    if num < len(less):
        return select(less,num)
    elif num < len(equal) + len(less):
        return equal[0]
    else:
        return select(more,num-len(less)-len(equal))
    
    
            
def sep(lst):
    ans = []
    temp = []
    for i in lst:
        if len(temp) == 4 or i == lst[-1]:
            temp.append(i)
            ans.append(temp)
            temp = []
        else:
            temp.append(i)
    return ans

def group_sort(lst):
    for i in range(len(lst)):
        #print(lst[i])
        lst[i].sort()

'''
def MoM(lst):
    temp = sorted(lst)
    return temp[len(temp)//2]
'''

'''
x = [10,1,0,11,3,9,20,12,7,8,17,6,2,14,19,18,21,16,15,13,5,4]
select(x,15)

y = sep(x)
group_sort(y)
print(y)
'''
A = list(range(222))
random.shuffle(A)
print([select(A,i) for i in range(222)])
