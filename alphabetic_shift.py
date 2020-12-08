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
'''
def alphabeticShift(inputString):

    for i, character in enumerate(inputString):
        if character == 'z':
            x = (inputString[i]).replace(f'{character}','a')
            print(x)
        else:
            (inputString[i]).replace(inputString[i],chr(ord(inputString[i]))),

    return inputString

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

