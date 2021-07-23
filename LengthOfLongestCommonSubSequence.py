str1 = input().strip()
str2 = input().strip()
table = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]
maxi_len = 0
for i in range(1,len(table)):
    for j in range(1,len(table[0])):
        if str1[i-1]==str2[j-1]:
            table[i][j]=1+table[i-1][j-1]
        else:
            table[i][j]=max(table[i-1][j],table[i][j-1])
print(table[-1][-1])
