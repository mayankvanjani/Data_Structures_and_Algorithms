'''
Mayank Vanjani mv1506
Homework 1
1/28/17
'''

#Question 1
'''
example1: O(n)
example2: O(n)
example3: O(n^2)
example4: O(n)
example5: O(n^3)
'''

#Question 2
def merge(l1, l2):
    answer = []
    for i in range(min(len(l1), len(l2))):
        answer.append(l1[i])
        answer.append(l2[i])
    if max(len(l1), len(l2)) == len(l1):
        extra = l1[min(len(l1), len(l2)):]
    else:
        extra = l2[min(len(l1), len(l2)):]
    for i in extra:
        answer.append(i)
    return answer;

#Question 3
class polynomial():
    def __init__(self, coefficient):
        self._coefficient = coefficient;
        
    def __str__(self):
        answer = ""
        for i in range(len(self._coefficient)):
            if i == len(self._coefficient)-1:
                answer += str(self._coefficient[i])
            else:
                answer += str(self._coefficient[i])+"x^"+str(len(self._coefficient)-1-i)+"+"
        return ("Polynomial Function: " + answer)
    
    def evaluate(self, var):
        answer = 0;
        for j in range(len(self._coefficient)):
            #print("i:", i, end="\t")
            #print("j:", j, end="\t")
            #print("num:", self._coefficient[j])
            answer += self._coefficient[j] * var ** (len(self._coefficient)-1-j)
        #print(answer)
        return answer
            
#Question 4
def f(n):
    return (1/pow(2, n))

def sigma(functions, a, b):
    answer = 0
    for i in range(a, b+1):
        answer += f(i)
    return answer

#MAIN
def main():
    print([i for i in merge( range(5), range(100, 105))])
    print([i for i in merge( range(5), range(100, 101))])
    print([i for i in merge( range(1), range(100, 105))])
    print()
    
    P = polynomial((6,2,1,8))
    print(str(P))
    print([P.evaluate(i) for i in range(10)])
    P_2 = polynomial((6,2,1,8,5,9))
    print(str(P_2))
    print([P_2.evaluate(i) for i in range(10)])

    print("\nSigma: i=2 to 10 of the function f(i)=1/2^i")
    print(sigma(f, 2, 10))
    
main();
