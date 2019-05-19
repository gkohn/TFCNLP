# -*- coding: utf-8 -*-
"""
Created on Sun May 19 19:16:06 2019

@author: grace.kohn
"""

import os
from textblob import TextBlob
import pandas as pd

# Set Male and Female Directories
dir_1 = 'C:/Users/grace.kohn/OneDrive - Accenture/2018 Sync/Stevens/FE 595 Spring 2019/TFC NLP/Female'
dir_2 = 'C:/Users/grace.kohn/OneDrive - Accenture/2018 Sync/Stevens/FE 595 Spring 2019/TFC NLP/Male'

# Load Merged Files
os.chdir(dir_1)
female = open("female_merge.txt", "r").read()
os.chdir(dir_2)
male = open("male_merge.txt", "r").read()

# Create Master File
master = male + female

# Define Function to Output List of Descriptors 
def Descriptors(File_name):
    tb_text = TextBlob(File_name)
    adj_list =[]
    # Once the TextBlob is created, a loop is performed over the list of words
    # to identify the descriptors (PoS like JJ are adjectives)
    for word,pos in tb_text.tags:
        if pos[0:2] =="JJ":
            adj_list.append(word)
    # Creating a Dataframe indicating how many times the adjective is on the list
    adj_list_df = pd.DataFrame({'Descriptor':adj_list})
    count_desc = adj_list_df['Descriptor'].value_counts(sort=False).sort_values(ascending=False)
    count_df = count_desc.rename_axis('Descriptor').reset_index(name='Occurences')
    return(count_df[0:10])

# Run
Descriptors(master)
