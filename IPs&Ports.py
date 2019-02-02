#!/usr/bin/env python
# coding: utf-8

# In[25]:


import re
list = []

with open(input("What file would you like to use? "), 'r') as file: 
    for line in file:
        line = line.strip('\n')
        line2 = re.split(':', line)
        line3 = line2[1:2]
        line4 = (', '.join(line3))
        list == list.append(line4)
list2 = ','.join(map(str,list))

with open(input("What do you want to call the new file? "), 'w') as the_file:
    the_file.write(list2)

