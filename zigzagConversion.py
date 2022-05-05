'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
'''
def convert(s,numRows):
    if len(s)==1 or numRows==1 or len(s)==numRows or numRows>len(s):return s
    d={}
    start=0
    end=len(s)
    ind=0
    while ind<end:
        if start==numRows-1:
            while start!=-1 and ind!=end:
                d[start]=d.get(start,'')+s[ind]
                start-=1
                if start==-1:
                    break
                ind+=1
            start=1
            ind+=1
        else:
            d[start]=d.get(start,'')+s[ind]
            start+=1
            ind+=1
    r=''.join(d[i] for i in range(numRows))
    return r
s=input()
numRows=int(input())
print(convert(s,numRows))