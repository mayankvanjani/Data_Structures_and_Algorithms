'''
Mayank Vanjani mv1506
Homework 12
5/2/17
'''

def lcs(A,B):
    if len(A) == 0 or len(B) == 0:
        return ""
    if A[0] == B[0]:
        return A[0] + lcs(A[1:],B[1:])
    else:
        sol1 = lcs(A[1:],B)
        sol2 = lcs(A,B[1:])
        if len(sol1) > len(sol2):
            return sol1
        else:
            return sol2

def make_scores():
    Scores={}
    import string
    for c in string.ascii_lowercase:
        Scores[c]=1
    for c in string.ascii_uppercase:
        Scores[c]=2
    return Scores

'''
def lcsScore(X,Y,scores):
    if len(X) == 0 or len(Y) == 0:
        return ("",0)
    if X[0] == Y[0]:
        new = lcsScore(X[1:],Y,scores)
        if X[0] not in scores:
            return (new[0],new[1])
        return (X[0]+new[0], new[1]+scores[X[0]])
    else:
        sol1 = lcsScore(X[1:],Y,scores)
        sol2 = lcsScore(X,Y[1:],scores)
        if sol1[1] > sol2[1]:
            return sol1
        else:
            return sol2
'''
'''
def lcsScore(X,Y,scores,i=0,j=0):
    if len(X) == i or len(Y) == j:
        return ("",0)

    if X[i] == Y[j]:
        new = lcsScore(X,Y,scores,i+1,j+1)
        if X[i] not in scores:
            return (new[0], new[1])
        return (X[i]+new[0], new[1]+scores[X[i]])
    else:
        sol1 = lcsScore(X,Y,scores,i+1,j)
        sol2 = lcsScore(X,Y,scores,i,j+1)
        if sol1[1] > sol2[1]:
            return sol1
        else:
            return sol2
'''

def lcsScore(X,Y,scores,i=0,j=0,D=None):
    if D == None:
        D = {}
    if len(X) == i or len(Y) == j:
        return ("",0)

    if X[i] == Y[j]:
        if (i+1,j+1) in D:
            new = D[(i+1,j+1)]
        else:
            new = lcsScore(X,Y,scores,i+1,j+1,D)
            D[(i,j)] = new
        if X[i] not in scores:
            return (new[0], new[1])
        return (X[i]+new[0], new[1]+scores[X[i]])
    else:
        if (i+1,j) in D:
            sol1 = D[(i+1,j)]
        else:
            sol1 = lcsScore(X,Y,scores,i+1,j,D)
            D[(i+1,j)] = sol1
        if (i,j+1) in D:
            sol2 = D[(i,j+1)]
        else:
            sol2 = lcsScore(X,Y,scores,i,j+1,D)
            D[(i,j+1)] = sol2
        if sol1[1] > sol2[1]:
            return sol1
        else:
            return sol2

Scores = make_scores()
print( sum(Scores[c] for c in "ab cdABC" if c in Scores ))
print()
#print(lcs("hello","hel"))

S1 = "hello"
S2 = "hel"
print(S1,"|",S2,lcsScore(S1,S2,Scores))
print()
S1 = "ab cdAB C"
S2 = "AB Cab cd"
print(S1,"|",S2,lcsScore(S1,S2,Scores))
print()

S1="""
  From fairest creatures we desire increase,
  That thereby beauty's rose might never die,
  But as the riper should by time decease,
  His tender heir might bear his memory:
  But thou, contracted to thine own bright eyes,
  Feed'st thy light's flame with self-substantial fuel,
  Making a famine where abundance lies,
  Thy self thy foe, to thy sweet self too cruel:
  Thou that art now the world's fresh ornament,
  And only herald to the gaudy spring,
  Within thine own bud buriest thy content,
  And tender churl mak'st waste in niggarding:
    Pity the world, or else this glutton be,
    To eat the world's due, by the grave and thee."""

S2="""  
  Look in thy glass and tell the face thou viewest
  Now is the time that face should form another;
  Whose fresh repair if now thou not renewest,
  Thou dost beguile the world, unbless some mother.
  For where is she so fair whose unear'd womb
  Disdains the tillage of thy husbandry?
  Or who is he so fond will be the tomb,
  Of his self-love to stop posterity?
  Thou art thy mother's glass and she in thee
  Calls back the lovely April of her prime;
  So thou through windows of thine age shalt see,
  Despite of wrinkles this thy golden time.
    But if thou live, remember'd not to be,
    Die single and thine image dies with thee."""
import sys
sys.setrecursionlimit(2000)
#print(S1)

print(lcsScore(S1,S2,Scores))
