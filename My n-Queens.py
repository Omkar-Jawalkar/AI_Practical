#!/usr/bin/env python
# coding: utf-8

# In[2]:


#  BAcktracking

N = int(input())
board = [[0]*N for i in range(N)]

def isattack(i,j):
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
        
    for k in range(0, N):
        for l in range(0,N):
            if (k+l == i+j) or (k-l == i-j):
                 if board[k][l] == 1:
                        return True
    return False
                

def NQueens(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if(not(isattack(i,j)) and (board[i][j]!=1)):
                board[i][j]=1
                if NQueens(n-1)==True:
                    return True
                board[i][j]=0


NQueens(N);
for i in board:
    print(i)


# In[6]:



N = int(input())
board = [[0]*N for i in range(N)]


def isattacked(i,j):
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l == i-j):
                if board[k][l]==1:
                    return True
    return False


def NQueens(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (not(isattacked(i,j)) and board[i][j]!=1):
                board[i][j]=1
                if NQueens(n-1) == True:
                    return True
                board[i][j]=0
    
NQueens(N)
for i in board:
    print(i)


# In[ ]:





# In[ ]:




