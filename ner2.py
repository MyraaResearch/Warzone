# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 21:05:04 2018

@author: gyand
"""
import os
java_path = "C:\\Program Files\\Java\\jdk1.8.0_151\\bin\\java.exe"
os.environ['JAVAHOME'] = java_path

import nltk
from nltk.tag import StanfordNERTagger
from nltk.metrics.scores import accuracy

raw_annotations = open("C:\\Users\\suman\\Desktop\\wikigold.conll.txt").read()
split_annotations = raw_annotations.split()

# Amend class annotations to reflect Stanford's NERTagger
for n,i in enumerate(split_annotations):
	if i == "I-PER":
		split_annotations[n] = "PERSON"
	if i == "I-ORG":
		split_annotations[n] = "ORGANIZATION"
	if i == "I-LOC":
		split_annotations[n] = "LOCATION"

# Group NE data into tuples
def group(lst, n):
    for i in range(0, len(lst), n):
        val = lst[i:i+n]
        if len(val) == n:
            yield tuple(val)

reference_annotations = list(group(split_annotations, 2))
pure_tokens = split_annotations[::2]
tagged_words = nltk.pos_tag(pure_tokens)
nltk_unformatted_prediction = nltk.ne_chunk(tagged_words)
				                     
stanford_prediction = st.tag(pure_tokens)
stanford_accuracy = accuracy(reference_annotations, stanford_prediction)
print(stanford_accuracy)

print(reference_annotations)
