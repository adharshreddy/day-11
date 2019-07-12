#!/usr/bin/env python
# coding: utf-8

# ### Dictionaries
# - It works on the concept of set unique data
# - keys,values is tyhe unique identifier for a value
# - Each Key is seperated from its values with a colom(:)
# - Each key and value is seperated by a comma(,)
# - Dictionaries enclosed with curly braces({})

# In[10]:


d1={"Name":"Gitam","Email id":"gitam@gmail.com","Address":"Hyderabad"}
print(d1)


# In[5]:


d1["Name"]


# In[12]:


d1['Email id']='gitampython@gmail.com'


# In[13]:


d1


# In[14]:


del d1['Email id']


# In[15]:


d1


# ### Contact Application
# * Add Contact
# * Search the Contact
# * List all contacts
#     * Name 1: Phone 1
#     * Name 2: Phone 2
# * Modify the contact
# * Remove the contact
# * Import the contact

# In[16]:


# Add Contact
contacts =  {}
def addcontact(name,phone):
    if name not in contacts:
        contacts[name]=phone
        print("Contact details are added")
    else:
        print("Contact already Exists")
    return
addcontact('tanishq','9573617180')
addcontact('tanishq jio','8919293845')
addcontact('tanishq jio','8919293845')
    


# In[18]:


#SEarch for contact details

def search(name):
    if name in contacts:
        print(name, " : " , contacts[name])
    else:
        print("%s does not exists"% name)
    return 
search('anil')
search('tanishq')
search('tanishq jio')


# In[22]:


#import some contacts
# Merge the contacts with existing one
def merge(newcontacts):
    contacts.update(newcontacts)
    print(len(newcontacts.keys()),"Contacts added Succesfully")
    return
newcontacts={'dheeraj':6300598900,'karthik':1234567890,'anurag': 1987654321,'saras':5432109876}
merge(newcontacts)


# In[27]:


contacts


# In[43]:


# Delete a contact
def delete(name,phone):
    if name in contacts:
        contacts[name]=phone
        
        print("updated succesfully")
    else:
        print(name,"not exists")
    return
delete('karthik',9272026881)


# In[44]:


contacts


# In[4]:


s1= 'GITAM'
print(s1.islower ())
print(s1.isupper ())


# In[5]:


s2='Python Programming'
s3='python Programming'
print(s2.istitle())
print(s3.istitle())


# In[7]:


s2='Application1889'
s3='PythonProgramming'
print(s2.isalpha())
print(s3.isalpha())


# In[10]:


s1='1234'
s2='Application1234'
print(s1.isnumeric ())
print(s2.isnumeric ())


# In[13]:


s1=' '
s2='Py th on'
print(s1.isspace())
print(s2.isspace())


# ### String Methods
# * 1. join()-- Method will concatinates the two strings
# * 2. split() -- returns the list of strings  seperated by whitespace(no parameters are given)
# * 3. replace() -- 

# In[14]:


s1='python'
print(" ".join(s1))


# In[15]:


s1='python Programming easy to learn'
print(", ".join(s1))


# In[16]:


s1=['python',"Programming","learn"]
print(", ".join(s1))


# In[17]:


s1='python Programming easy to learn'
print(s1.split())


# In[21]:


s1='python Programming easy to learn'
print(s1.split('m'))


# In[22]:


s1='python Programming easy to learn'
li=s1.split()
print(li)


# In[23]:


s1='python Programming easy to learn'
li=s1.split()
print(li)
print(len(li))


# In[24]:


s1='python Programming easy to learn'
li=list(s1)
print(li)


# In[27]:


s1='python Programming easy to learn'
print(s1.replace("python","C"))


# In[ ]:




