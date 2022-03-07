#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing Libraries and reading Dataset
import pandas as pd

df = pd.read_excel('skill_data.xlsx')

df.head()


# In[2]:


# Skills To Assign Designation

web_devloper_skills = [
    'django',
    'html',
    'css',
    'nodejs',
    'reactjs',
    'nodejs',
    'flask',
    'laravel'
]

machine_learning_skills = [
    'nosql',
    'pandas',
    'numpy',
    'matpotlib',
    'seabron',
    'scipy'
]


# In[3]:


df.info()


# In[4]:


# The Function will assign role, based on at least 3 skills(ML/Web) and return dataframe
def Assign_designation(df):
    List = []

    for i in df['Skills']: # i ex: "['reactjs', 'django', 'numpy', 'nodejs', 'html','django','numpy']"

        d = set(eval(i)) # remove duplicates from i and eval [['reactjs', 'django', 'numpy', 'nodejs', 'html']]
        w=0
        m=0

        if len(d)<=2:
            List+=["Not Elgible"]
        else:
            for j in d:
                if j in web_devloper_skills:
                    w+=1
                elif j in machine_learning_skills:
                    m+=1

            if w>m and w>=3:
                List+=["Web Developent"]
            elif m>w and m>=3:
                List+=["Machine Learning"]
            elif w==3 and m==3:
                List=["Equal"]
            else:
                List+=["Not Elgible"]

    df["Designation"] = List
    df.loc[len(df.index)]  = ["Total : ",len(web_devloper_skills)+len(machine_learning_skills),'']

    return df
                
            
        


# In[5]:


# Calling Function
print(Assign_designation(df))
df.to_excel("Output.xlsx",index=False)


