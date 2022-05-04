'''
Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

def lls(s):
    if s=='':
        return 0
    if len(s)==len(set(s)):
        return len(set(s))
    k=[]
    sub=''
    start=0
    end=len(s)
    index=0
    while start<end:
        if s[start] not in sub:
            sub+=s[start]
            start+=1
        else:
            index+=1
            sub=''
            start=index
        k.append(sub)
    return len(sorted(k,key=len)[-1])
s=input()
print(lls(s))