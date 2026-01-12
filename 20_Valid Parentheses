'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        dic : dict[str, str] = {"(":"a",")":"aa","[":"b","]":"bb","{":"c","}":"cc"}
        # store open parentheses in cur
        cur : str = ""
        for i in s:
            # if closed, check if current type of parentheses was last added
            if (len(dic[i]) == 2):
                if (cur == "" or cur[-1] != dic[i][0]):
                    return False
                # if valid, remove from cur
                cur = cur[:-1]
            # if open, add to cur
            else:
                cur += dic[i]
        # no open parenthesis at the end
        return cur == ""