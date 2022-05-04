'''
Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
'''
def longestPalindrome(s):
    r=[]
    if s==s[::-1]:
        return s
    if len(s)==len(set(s)):
        r=[i for i in s]
    start=0
    end=len(s)-1
    while start<end:
        if s[start]==s[end] and s[start:end+1]==s[start:end+1][::-1]:
            r.append(s[start:end+1])
            start+=1
            end=len(s)-1
        else:
            end-=1
            if end==start:
                start+=1
                end=len(s)-1
    r=[i for i in s]
    return max(r,key=len)
s=input()
print(longestPalindrome(s))
