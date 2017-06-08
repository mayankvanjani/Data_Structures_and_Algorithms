'''
Mayank Vanjani mv1506
Homework 4
2/21/17
'''

def insomewhere(X, s):
    for i in X:
        #print("Element:", i)
        if isinstance(i, list):
            #print("SubList:", i)
            if insomewhere(i,s):
                return True
        else:
            if i==s:
                return True
            #print("Normal:", i)
    return False
            
def unnest(A, ans=None):
    if ans == None:
        ans = []
    for i in A:
        if isinstance(i, list):
            #print("i:", i)
            ans += unnest(i)
            #print("ans:", ans)
        else:
            #print(i)
            ans += [i]
    return ans

def print2D(A):
    ans = "[\n"
    for i in A:
        ans += (" " + str(i) + "\n")
    ans += "]"
    print(ans)

def triangle(n):
    ans = []
    for i in range(n,0,-1):
        ans += [[i for i in range(n,i-1,-1)]]
    return(ans)

def table(coef,exp):
    ans = []
    for j in exp:
        ans += [[pow(i,j) for i in coef]]
    return ans

def nest(elem, lsts):
    if lsts == 0:
        return elem
    else:
        return [nest(elem,lsts-1)]

def main():

    A=[[1,2],[3,[[[4],5]],6],7,8]
    print("A:",A)
    print("6 in A?", insomewhere(A,6)) #True
    print("66 in A?", insomewhere(A,66)) #False
    print()

    A=[[1,2],[3,[[[4],5]],6],7,8]
    B = [[[1]]]
    print(A, "\nUnNested:", unnest(A))
    print(B, "\nUnNested:", unnest(B))
    print()

    print("Testing 2D Printing:")
    print2D([[i]*10 for i in range(10)])
    print()

    print("Testing Triangle 2D Printing (5 and 10):")
    print2D(triangle(5))
    print2D(triangle(10))
    print()

    print("Power Tables:")
    print("Power Table of [1,2,10] in range(10,15)")
    print2D(table([1,2,10],range(10,15)))
    print()

    print("Nesting:")
    print(nest("nest",2))
    print(nest(53,10))
    print(unnest(nest(53,10)))
    print(unnest(nest("nest",2)))
    print()


    
    #~~~~~~~~~~#
    #Question 7#
    print("Question 7 Answer: A = [[1],[1]]*5 =>")

    A =[[1],[1]]*5

    print(A)
    A[3][0] = 5
    print(A)
    
main()

