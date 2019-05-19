# -*- coding: utf-8 -*-
"""
Created on Sat May 18 16:22:43 2019

@author: grace.kohn
"""

import os

# Set Male and Female Directories
dir_1 = 'C:/Users/grace.kohn/OneDrive - Accenture/2018 Sync/Stevens/FE 595 Spring 2019/TFC NLP/Female'
dir_2 = 'C:/Users/grace.kohn/OneDrive - Accenture/2018 Sync/Stevens/FE 595 Spring 2019/TFC NLP/Male'

# Save File Names
files_f = next(os.walk(dir_1))[2]
files_m = next(os.walk(dir_2))[2]

# Create Male and Female Placeholder Buckets
male = []
female = []

# Define function to load data
def load(fname):
    f = open(fname,'r')
    data = []
    for line in f.readlines():
        data.append(line.replace('\n','').split('\n'))
    f.close()
    return data

### Female ####

#Set Working Directory to Female Files
os.chdir(dir_1)

for i in range(0,(len(files_f))):
    temp = load(files_f[i])
    if temp[0][0][0] == '[':
        temp = temp[0]
        for item in temp:
                female.append(item[0])
    elif temp[0][0][0] == 'A':
        for item in temp:
                temp_str = item[0]
                female.append("She's "+temp_str.lower())
    else:
        for item in temp:
            female.append(item[0])
        
        
with open('female_merge.txt', 'w') as f:
    for listitem in female:
        f.write('%s\n' % listitem)
        
        
### Male ####

#Set Working Directory to Male Files
os.chdir(dir_2)

for i in range(0,(len(files_m))):
    temp = load(files_m[i])
    if temp[0][0][0] == '[':
        temp = temp[0]
        for item in temp:
                male.append(item[0])
    elif temp[0][0][0] == 'A':
        for item in temp:
                temp_str = item[0]
                male.append("He's "+temp_str.lower())
    else:
        for item in temp:
            male.append(item[0])
        
        
with open('male_merge.txt', 'w') as f:
    for listitem in male:
        f.write('%s\n' % listitem)
