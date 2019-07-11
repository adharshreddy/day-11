#!/usr/bin/env python
# coding: utf-8

# In[2]:


# function to create a file and write to the file
def createfile(filename):
    f = open(filename,'w')
    for i in range(10):
        f.write('this is %d line'% i)
    print("file is created and data has written")
    return
createfile('file1.txt')


# In[5]:


def createfile(filename):
    f = open(filename,'w')
    f.write('Testing...\n')
    print("file is created and data has written")
    return
createfile('file1.txt')


# In[6]:


def appendData(filename):
    f = open(filename,'a')
    f.write("new line 1 \n")
    f.write("new line 2 \n")
    print("file created and successfully data written")
    return
appendData('file2.txt')


# In[7]:


# function to read of the file
def readFileData(filename):
    f = open(filename,'r')
    if f.mode == 'r':
        x = f.read()
        print(x)
    f.close()
    return
readFileData('file2.txt')


# In[9]:


# function to read th file
def fileoperations(filename,mode):
    with open(filename,mode) as f:
        if f.mode == 'r':
            data = f.read()
            print(data)
        elif f.mode == 'a':
                f.write('dara to the file')
                print('the data is successfully written')
        f.close()
        return
filename = input('enter the file name')
fileoperations(filename,mode)


# In[ ]:


# data analysis
# word count program
def wordcount(filename,word):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x = f.read()
            li = x.split()
    cnt = li.count(word)
    return cnt
filename = input('enter the file name:')
word = input('enter the word:')
wordcount(filename,word)


# In[ ]:


# data analysis
# word count program
def wordcount(filename,word):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x = f.read()
            li = x.split() 
    cnt = li.count(word)
    return cnt
filename = input('enter the file name:')
word = input('enter the word:')
wordcount(filename,word)


# In[ ]:


# character count from the given file
def charcount(filename):
    with open(filename,'r')as f:
        if f.mode == 'r':
            x = f.read()
            li = list(x)
    retutn len(li)
filename


# In[1]:


# function to find the no of lines in the input file
# input ...filename(file2.txt)
# output...no of lines(12)
def countoflines(filename):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x = f.read()
            li = x.split("\n")
    return len(li)
filename = input('enter the filename :')
countoflines(filename)


# In[2]:


# function to print the upper and lower character
def casecount(filename):
    cntupper = 0
    cntlower = 0
    with open(filename,'r') as f:
        if f.mode =='r':
            x = f.read()
            li = list(x)
    for i in li:
        if i.isupper():
            cntupper += 1 # cntupper = cntupper + 1
        elif i.islower():
            cntlower += 1 # cntlower = cntlower +1
    output = 'upprer case = {0}, lower case = {1}'.format(cntupper,cntlower)
    return output
filename = input('enter the filename :')
casecount(filename)


# In[ ]:


# math,random,

