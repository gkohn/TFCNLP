# -*- coding: utf-8 -*-
"""
Created on Sun May 19 17:50:04 2019

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

# Define function to find polarity of sentiment
def identify_sentiment(text_input):
    blob = TextBlob(text_input)
    sentences = blob.sentences
    sent_out = []
    for sentence in sentences:
        sent_out.append(TextBlob(str(sentence)).sentiment.polarity)
    sent_out = pd.DataFrame(sent_out)
    index_positive = sent_out.idxmax()[0]
    index_negative = sent_out.idxmin()[0]
    return str(sentences[index_positive]), str(sentences[index_negative])

# Combine positive and negative into original format
def output_polar(female_file, male_file):
    female_out = identify_sentiment(female)
    male_out = identify_sentiment(male)
    positive = male_out[0] + ' ' + female_out[0] + ' They Fight Crime!'
    negative = male_out[1] + ' ' + female_out[1] + ' They Fight Crime!'
    return positive, negative


# Run scripts
output_polar(female, male)