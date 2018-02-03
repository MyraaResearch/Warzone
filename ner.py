# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 20:53:50 2018

@author: gyand
"""
import os
java_path = "C:\\Program Files\\Java\\jdk1.8.0_151\\bin\\java.exe"
os.environ['JAVAHOME'] = java_path

from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize


st = StanfordNERTagger('C:\\Users\\suman\\Desktop\\hack\\stanford-ner-2017-06-09\\classifiers\\english.all.3class.distsim.crf.ser.gz',
					   'C:\\Users\\suman\\Desktop\\hack\\stanford-ner-2017-06-09\\stanford-ner-3.8.0.jar',
					   encoding='utf-8')

text = 'While in France, Christine Lagarde, Nikita discussed short-term stimulus efforts in a recent interview with the Wall Street Journal .'

tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)

print(classified_text)