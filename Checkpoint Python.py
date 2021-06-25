#!/usr/bin/env python
# coding: utf-8
Question 1
# In[ ]:


liste=[]
for x in range(2000, 3000):
      if (x%7==0) and (x%5!=0): 
        liste.append(str(x))
print (','.join(liste))

Question 2
# In[134]:


def factorial(n):
    fact = 1
    for  num in range(2, n + 1):
        fact = fact*num
    return fact
    if n==0:
        print (1)
    elif n<0:
        print("the factorial does not exist")   


# In[136]:


factorial(-9)

Question 3
# In[ ]:


n = int(input("Enter the value of n: "))
squares = {i : i*i for i in range(1, n+1)}
print(squares)

Question 4
# In[ ]:


def missing_char(str, n):
  front = str[:n]   
  back = str[n+1:]  
  return front + back

Question 5

# In[ ]:


import numpy as np
x= np.arange(6).reshape(3, 2)
print("Original array elements:")
print(x)
print("Array to list:")
print(x.tolist())

Question 6
# In[ ]:


import numpy as np
x= np.arange(3)
print("Original array 1:")
print(x)
print("Original array 2:")
print(x.tolist())

Question 7
# In[ ]:


numbers = input("Provide a: ")
numbers = numbers.split(',')

result_list = []
for a in numbers:
    b = round(math.sqrt(2 * 50 * int(a) / 30))
    result_list.append(b)

print(result_list)


# In[ ]:




