Recall that if you were to run the LCS algorithm on the strings "ab cdABC" and "ABCab cd" it would return "ab cd"
 
Your task is to code a weighed version of this problem. Suppose, for example, that uppercase characters should be worth twice that of lowercase characters, and that non-letter characters should be ignored. We will represent this as a dictionary, where characters are assigned a score. Those characters not in the dictionary are to be ignored. 
 
For example, if uppercase characters should be worth twice that of lowercase characters, and non-letter characters should be ignored, we could create the following dictionary:
 
Scores={}
import string
for c in string.ascii_lowercase:
    Scores[c]=1
for c in string.ascii_uppercase:
    Scores[c]=2
 
The score of a string could be computed as follows:
 
print( sum(Scores[c] for c in "ab cdABC" if c in Scores ))
>> 10
 
Your task is to code lcsScore(X,Y,Scores) that given strings X and Y, returns the common subsequence of X and Y with the highest score, using the Scores dictionary. Specifically, it should return a tuple of the string with the highest score, and the score.
 
print(lcsScore("ab cdAB C","AB Cab cd",Scores))
('ABC', 6)
 
Note that the normal LCS of these strings is different: "ab cd", but the score of this string is only 4, and is lower than "ABC" which scores 6.
 
 
Your code should run in time O(len(X)⋅len(Y)). I encourage you to follow the steps we have been using to solve these problems:
 
Code a simple but slow recursive program using slices
Get rid of the slices
Use dynamic programming to avoid duplicate recursive calls
 
Here is a longer test case:
 
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

S2="""  Look in thy glass and tell the face thou viewest
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
print(lcsScore(S1,S2,Scores))
Should print:
('oitasdeecetheetosetietateshouldmaterherheariothouotrtdttheonbheFeeshsfawhseubsantillagfanwhendlethetohseetstoorThouattotherldshenthealtoeypriiththinowsthneehltseitewrlesthisgluttobeotteldthegedthee', 199)
