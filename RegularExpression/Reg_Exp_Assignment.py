#!/usr/bin/env python
# coding: utf-8

# In[69]:


# Question 1 Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
# Sample Text-'Python Exercises, PHP exercises.'

import re
sample_text= "Python Exercises, PHP exercises."
print(re.sub("[ ,.]", ":", sample_text))


# In[70]:


#Question 2 Write a Python program to find all words starting with 'a' or 'e' in a given string

import re
sample_text= "I am Chaitanya, this is an extra RE assignment."
aewordlist = re.findall(r"\b[ae]\w+", sample_text)
print(aewordlist)


# In[67]:


#Question 3 Create a function inpython to find all words that are at least 4 characters long in a string.
#The use of the re.compile() method is mandatory.

import re
sample_text = "I am Chaitanya, this is an extra RE assignment."
str_pattern= re.compile(r"\b\w{4,}\b")
print(str_pattern.findall(sample_text))


# In[66]:


#Question 4 Create a function in python to find all three, four, and five character words in a string. 
#The use of the re.compile() method is mandatory.

import re
sample_text = "I am Chaitanya, this is an extra REX assignment."
str_pattern= re.compile(r"\b\w{3,5}\b")
print(str_pattern.findall(sample_text))


# In[65]:


#Question 5 Create a function in Python to remove the parenthesis in a list of strings.The use of the re.compile() method is mandatory.
#Sample Text:["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

import re
sample_list= ["example(.com)","hr@fliprobo(.com)","github(.com)","Hello(Data Science World)","Data (Scientist)"]
sample_str = ' '.join(sample_list)
print(re.sub("[()]", "", sample_str))


# In[56]:


# Question 11 Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

import re
sample_text = "I_am_Chaitanya_age_75"
str_pat = '^[a-zA-Z0-9_]*$'
matched_str = re.search(str_pat,sample_text)
print(matched_str)


# In[170]:





# In[54]:


#Question 12 Write a Python program where a string will start with a specific number

import re
def match_my_str(string):
    text = re.compile(r"^0")
    if text.match(string):
        return True
    else:
        return False
print(match_my_str('0 is important number in mathematics'))
print(match_my_str('This is 5 star hotel'))


# In[52]:


#Question 13 Write a Python program to remove leading zeros from an IP address
import re
ip = "10.02.035.132"
rem_string = re.sub('\.[0]*', '.', ip)
print(rem_string)


# In[51]:


#Question 15 Write a Python program to search some literals strings in a string. 
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox', 'dog', 'horse'

import re
animals = ['fox','dog','horse']
sample_text = "'The quick brown fox jumps over the lazy dog"
for i in animals:
    if re.search(i,sample_text):
        print("Literal String "  + i + " found in the string")
    else:
        print("Literal string " + i +" not found in the string")


# In[107]:





# In[142]:


#Question 16
#Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : Fox

import re
sample_text = "'The quick brown fox jumps over the lazy dog"
find_match = re.search('fox',sample_text)
print(find_match.group())
print(find_match.span())


# In[50]:


#Question 17 Write a Python program to find the substrings within a string.
#Sample text : 'Python exercises, PHP exercises, C# exercises'

import re
sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for i in re.findall(pattern,sample_text):
    print("substring found :" + i)


# In[47]:


#Question 18 Write a Python program to find the occurrence and position of the substrings within a string.

import re
sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern='exercises'
for find_match in re.finditer(pattern,sample_text):
    start_char = find_match.start()
    end_char = find_match.end()
    print("Location start of substring "+str(start_char))
    print("Location end of substring " +str(end_char))


# In[43]:


#Question 19 Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

import re
def change_date_format(sample_date):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1',sample_date)
print("Formatted date in DD-MM-YYYY :",change_date_format('1982-01-11'))


# In[36]:


# Question 20 Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string.
# The use of the re.compile() method is mandatory.

def check_decimal(sample_number):
    import re
    pattern = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
    if pattern:
        decimal_number = pattern.search(sample_number)
        return decimal_number
    else:
        return 'none'
print(check_decimal('100.55'))


# In[71]:


# Question 21 Write a Python program to separate and print the numbers and their position of a given string.
import re
sample_text = "There are 50 balls in 2 new baskets"
for num_iter in re.finditer("\d+", sample_text):
    print(num_iter.group())
    print("Position start is:",+ num_iter.start())
    print("Position end is:",+ num_iter.end())


# In[213]:


# Question 22 Write a regular expression in python program to extract maximum/largest numeric value from a string.
# Sample Text: 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'

import re
sample_text = "My marks in each semester are: 947, 896, 926, 524, 734, 950, 642"
num =re.findall("\d+",sample_text)
print(max(num))


# In[215]:


# Question 23 Write a function in python to insert spaces between words starting with capital letters.
# Sample Text: “RegularExpressionIsAnImportantTopicInPython"

import re
def add_spaces(sample_text):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", sample_text)

print(add_spaces("RegularExpressionIsAnImportantTopicInPython"))


# In[30]:


# Question 24 Python regex to find sequences of one upper case letter followed by lower case letters
import re
sample_text ='Iamfine'
str_pat = '[A-Z]+[a-z]+$'
matched_str = re.search(str_pat,sample_text)
print(matched_str)


# In[32]:


#Question 26 Write a python program using RegEx to accept string ending with alphanumeric character.

import re
regex_expression = '[a-zA-z0-9]$'

def check_string(my_string):
   if(re.search(regex_expression, my_string)):
      print("The string ends with alphanumeric character")
   else:
      print("The string doesnot end with alphanumeric character")
        
print(check_string('Marks obtained is 70%'))


# In[233]:


import re
file = open(r"c:\desktop\dates.txt",'r')
sample_text = file.read()
date_matches = re.findall(r'(\d+/\d+/\d+)',sample_text)
print(date_matches)


# In[58]:


#Question 7 Write a regular expression in Python to split a string into uppercase letters.
#Sample text: “ImportanceOfRegularExpressionsInPython”

import re
sample_text = "ImportanceOfRegularExpressionsInPython"
print(re.findall('[A-Z][^A-Z]*', sample_text))


# In[33]:


#Question 8 Create a function in python to insert spaces between words starting with numbers.
#Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"

import re
def num_spaces(sample_text):
  return re.sub(r"(\w)([1-9])", r"\1 \2", sample_text)

print(num_spaces("RegularExpression1IsAn2ImportantTopic3InPython"))


# In[34]:


#Question 9 Create a function in python to insert spaces between words starting with capital letters or with numbers.
#Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"


import re
def cap_word_spaces(sample_text):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", sample_text)

print(cap_word_spaces("RegularExpression1IsAn2ImportantTopic3InPython"))


# In[64]:


# Question 6 Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
# Sample Text:["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

import re
    
with open(r"C:\Users\chait\Downloads\Test1.txt", "rt") as f:
    input = f.read()
    print(input)
    output = re.sub(r" ?\([^)]+\)", "",input)
    print(output)


# In[57]:


# Question 10 Write a python program to extract email address from the text stored in the text file using Regular Expression.
#Sample Text- Hello my name is Data Science and my email address is xyz@domain.com and alternate email address is xyz.abc@sdomain.domain.com. Please contact us at hr@fliprobo.com for further information.

import re
with open(r"C:\Users\chait\Downloads\Test2.txt", "rt") as f:
    input = f.read()
    output = re.findall('\S+@\S+',input) 
    print(output)


# In[28]:


# Question 25 Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
# Sample Text:"Hello hello world world"

import re
def duplicate_words(sample_text):
  return re.sub(r'\b(\w+)\b(?:\s+\1)+', r'\1',sample_text)

print(duplicate_words("Hello hello world world"))


# In[27]:


# Question 27 Write a python program using RegEx to extract the hashtags.
# Sample Text: """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""

import re
sample_text ="""RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
output=re.findall(r'#\w+',sample_text)
print(output)


# In[25]:





# In[24]:


#Question 28 Write a python program using RegEx to remove <U+..> like symbols
#Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.

import re
with open(r"C:\Users\chait\Downloads\Test4.txt", "rt") as f:
    input = f.read()
    output = re.findall('\S+@\S+',input) 
    print(output)


# In[21]:


#Question 29 -Write a python program to extract dates from the text stored in the text file.
#Sample Text:Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.

import re
with open(r"C:\Users\chait\Downloads\Test4.txt", "rt") as f:
    input = f.read()
    output = re.findall(r'\d{2}[/-]\d{2}[/-]\d{4}',input)
print(output)


# In[20]:


#Question 30 - Create a function inpython to remove all words from a string of length between 2 and 4.

import re
def remove_words(sample_text):
    str_pattern = re.compile(r'\W*\b\w{2,4}\b')
    rem_words =str_pattern.sub('',sample_text)
    return rem_words

print(remove_words("The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."))


# In[ ]:





# In[ ]:




