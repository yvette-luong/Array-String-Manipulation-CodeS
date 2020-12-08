'''
You are given a parentheses sequence, check if it's regular.

--Example
For s = "()()(())", the output should be
validParenthesesSequence(s) = true;
For s = "()()())", the output should be
validParenthesesSequence(s) = false.

--Input/Output

[execution time limit] 4 seconds (py3)

[input] string s
A string, consisting only of '(' and ')'.

Guaranteed constraints:
0 ≤ s.length ≤ 105.

[output] boolean

true is the sequence is regular and false otherwise.
'''
def validParenthesesSequence(s): 
    list = []

    for character in list:
        if character in ["(","{","["]:

            list.append(character)
        else: 
            if not list:
                return False
            current_char = list.pop()
            if current_char == "(":
                if character != ")":
                    return False 
            if current_char == "{":
                if character != "}":
                    return False
            if current_char == "[":
                if character != "]":
                    return False

    if list:
        return False
    return True