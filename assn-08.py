# coding: utf-8

# In[9]:

# The concert
# assn_08

import re
concert = open("the_concert.txt", 'r') #the concert text file
file_contents =concert.read()
print(file_contents)


# In[10]:

# Solution 1 (my fav) - print all matches that contain "ath"
x = re.findall("\w+ath\w+", file_contents)

print(x)
print("There are " + str(len(x)) + " forms of Katherine in this story")


# In[11]:

# Solution 2 - Basic. if matches are found, print "Found a match"
# This only works if you are interested in finding a match, not if you want the # or list 
match = re.search("\w+ath\w+", file_contents)

if match:
    print("Found a match:", match.group())
else:
    print ("No match:", match)



