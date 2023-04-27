#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for i in x:
    #i = [1,2,3,4]
    for j in i:
        
        if j%3==0:
            break
        print(j,end = ' ')
        
        
    print('hello')
    print()


# In[ ]:

ouput: 

1 2 hello

5 hello

hello

13 14 hello



