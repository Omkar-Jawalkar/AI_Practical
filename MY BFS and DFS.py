#!/usr/bin/env python
# coding: utf-8

# In[8]:


graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = []
queue = []

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        n = queue.pop(0)
        print(n + " ")
        
        for neighbour in graph[n]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
bfs([],graph,'5');


# In[9]:


graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set()

def dfs(visited,graph,node):
    if node not in visited:
        visited.add(node)
        print(node)
        
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
            
dfs(visited,graph,'5')
    


# In[ ]:




