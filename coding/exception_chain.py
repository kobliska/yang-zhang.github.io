
# coding: utf-8

# # Exception Chain

# ## First example
# A function that handles exception by writing to a logfile.

# Remove logfile if already exsits.

# In[68]:

rm -f logfile.txt


# In[69]:

def get_value(dictionary, name):
    try:
        return dictionary[name]
    except Exception as e:
        print("exception hit..writing to file")
        log = open('logfile.txt', 'w')
        log.write('%s\n' % e)
        log.close()


# In[70]:

names={"Jack":113, "Jill":32,"Yoda":395}


# In[71]:

print(get_value(names,"Jackz"))#change to Jack and it runs fine


# In[72]:

print(get_value(names,"Jack"))#change to Jack and it runs fine


# Change logfile to read-only

# In[73]:

ls -l logfile.txt


# In[74]:

get_ipython().system('chmod 400 logfile.txt')


# In[75]:

ls -l logfile.txt


# ```py
# KeyError: 'Jackz'
# 
# During handling of the above exception, another exception occurred: PermissionError: [Errno 13] Permission denied: 'logfile.txt'
# ```

# In[76]:

print(get_value(names,"Jackz"))


# ## Another example

# In[ ]:

def validate(value, validator):
    try:
        validator(value)
    except Exception as e:
        raise ValueError('Invalid value: %s' % value)
def validator(value):
    if len(value) > 10:
        raise ValueError("Value can't exceed 10 characters")


# In[ ]:

validate('ok', validator)


# ```py
# ValueError: Value can't exceed 10 characters
# 
# During handling of the above exception, another exception occurred: ValueError: Invalid value: tooooooo_long
# ```

# In[ ]:

validate('tooooooo_long', validator)


# Using `raise ... from`

# In[ ]:

def validate(value, validator):
    try:
        validator(value)
    except Exception as e:
        raise ValueError('Invalid value: %s' % value) from e
def validator(value):
    if len(value) > 10:
        raise ValueError("Value can't exceed 10 characters")


# ```py
# ValueError: Value can't exceed 10 characters
# 
# The above exception was the direct cause of the following exception: ValueError: Invalid value: tooooooo_long
# ```

# In[ ]:

validate('tooooooo_long', validator)


# ```py
# TypeError: object of type 'int' has no len()
# 
# The above exception was the direct cause of the following exception: ValueError: Invalid value: 12345
# ```

# In[78]:

validate(12345, validator)


# The outmost exception is being raised.

# In[79]:

try:
    validate(12345, validator)
except Exception as e:
    print(e.__context__)
    print(type(e))


# Reference: Pro Python 2nd Edition

# In[ ]:

[Home](https://yang-zhang.github.io/)

