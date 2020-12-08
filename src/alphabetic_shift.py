'''
Given a string, 
your task is to replace each of its characters by the next one in the English alphabet; 
i.e. replace a with b, 
replace b with c, 
etc (z would be replaced by a).

--Example
For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".

--Input/Output
[execution time limit] 4 seconds (py3)

[input] string inputString
A non-empty string consisting of lowercase English characters.
Guaranteed constraints:
1 ≤ inputString.length ≤ 1000.

[output] string

The resulting string after replacing each of its characters.
# not work yet ! 
# def alphabeticShift(inputString):

#     for i, character in enumerate(inputString):
#         if character == 'z':
#             x = (inputString[i]).replace(f'{character}','a')
#             print(x)
#         else:
#             y = (inputString[i]).replace(inputString, (inputString[i] + 1)),
#             print(y)
#     return inputString
'''
def alphabeticShift(inputString):

    for i, character in enumerate(inputString):

        if character == 'z':
            charsToNumberList = [ord(i)+1 for i in inputString]
            # print(charsToNumberList)

        else:
            y = "".join([chr(ord(i)+1) for i in inputString])
            x = y.replace("{", "a")
    return x
'''
this is second solution : 
-----------------------

def alphabeticShift(inputString):
    new_inputString = ''
    for i, character in enumerate(inputString):
         if character == 'z':
             new_inputString += 'a'
         else:
             new_inputString += chr(ord(inputString[i])+1)
     return new_inputString 
     
-----------------------
'''

'''
INPUT to test for OUTPUT:
'''
inputString = ["c","r","a","z","y"]
# inputString = ["s","c","h","o","o","l"]
# inputString = ["y", "v", "e", "t", "t", "e"]

print(alphabeticShift(inputString))

