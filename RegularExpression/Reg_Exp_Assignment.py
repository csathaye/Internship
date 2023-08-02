#!/usr/bin/env python
# coding: utf-8

# In[51]:


import re
sample_text= "I am Chaitanya,This is re assignment."
print(re.sub("[ ,.]", ":", sample_text))


# In[48]:


import re
sample_text= "I am Chaitanya, this is an extra RE assignment."
aewordlist = re.findall(r"\b[ae]\w+", sample_text)
print(aewordlist)


# In[44]:


import re
sample_text = "I am Chaitanya, this is an extra RE assignment."
str_pattern= re.compile(r"\b\w{4,}\b")
print(str_pattern.findall(sample_text))


# In[43]:


import re
sample_text = "I am Chaitanya, this is an extra REX assignment."
str_pattern= re.compile(r"\b\w{3,5}\b")
print(str_pattern.findall(sample_text))


# In[68]:


import re
sample_list= ["example(.com)","hr@fliprobo(.com)","github(.com)","Hello(Data Science World)","Data (Scientist)"]
sample_str = ' '.join(sample_list)
print(re.sub("[()]", "", sample_str))


# In[80]:


import re
sample_text = "I_am_Chaitanya_age_75"
str_pat = '^[a-zA-Z0-9_]*$'
matched_str = re.search(str_pat,sample_text)
print(matched_str)


# In[170]:





# In[103]:


import re
def match_my_str(string):
    text = re.compile(r"^0")
    if text.match(string):
        return True
    else:
        return False
print(match_my_str('0 is important number in mathematics'))
print(match_my_str('This is 5 star hotel'))


# In[106]:


import re
ip = "10.02.035.132"
rem_string = re.sub('\.[0]*', '.', ip)
print(rem_string)


# In[119]:


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


import re
sample_text = "'The quick brown fox jumps over the lazy dog"
find_match = re.search('fox',sample_text)
print(find_match.group())
print(find_match.span())


# In[141]:


import re
sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for i in re.findall(pattern,sample_text):
    print("substring found :" + i)


# In[153]:


import re
sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern='exercises'
for find_match in re.finditer(pattern,sample_text):
    start_char = find_match.start()
    end_char = find_match.end()
    print("Location start of substring "+str(start_char))
    print("Location end of substring " +str(end_char))


# In[159]:


import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
sample_date = "2026-01-02"
print("Date entered in YYYY-MM-DD Format:",sample_date)
print("Formatted date in DD-MM-YYYY :",change_date_format(dt1))


# In[202]:


def check_decimal(sample_number):
    import re
    pattern = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
    if pattern:
        decimal_number = pattern.search(sample_number)
        return decimal_number
    else:
        return 'none'
print(check_decimal('100.555'))


# In[210]:


import re
sample_text = "There are 50 balls in 2 new baskets"
for num_iter in re.finditer("\d+", sample_text):
    print(num_iter.group())
    print("Position start is:",+ num_iter.start())
    print("Position end is:",+ num_iter.end())


# In[213]:


import re
sample_text = "My marks in each semester are: 947, 896, 926, 524, 734, 950, 642"
num =re.findall("\d+",sample_text)
print(max(num))


# In[215]:


import re
def add_spaces(sample_text):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", sample_text)

print(add_spaces("RegularExpressionIsAnImportantTopicInPython"))


# In[219]:


import re
sample_text ='Iamfine'
str_pat = '[A-Z]+[a-z]+$'
matched_str = re.search(str_pat,sample_text)
print(matched_str)


# In[232]:


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


# In[235]:


import re
sample_text = "ImportanceOfRegularExpressionsInPython"
print(re.findall('[A-Z][^A-Z]*', sample_text))


# In[241]:


import re
def num_spaces(sample_text):
  return re.sub(r"(\w)([1-9])", r"\1 \2", sample_text)

print(num_spaces("RegularExpression1IsAn2ImportantTopic3InPython"))


# In[242]:


import re
def cap_word_spaces(sample_text):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", sample_text)

print(cap_word_spaces("RegularExpression1IsAn2ImportantTopic3InPython"))


# In[ ]:




