
# coding: utf-8

# In[27]:

# The concert
# assn_08

import re
concert = open("the_concert.txt", 'r')
file_contents =concert.read()
print(file_contents)


# In[28]:

# print all matches that contain "ath"
x = re.findall("ath", file_contents)
print(x)


# In[ ]:



