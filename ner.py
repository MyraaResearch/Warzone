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

text = """In 1980, Samsung acquired the Gumi-based Hanguk Jeonja Tongsin and entered telecommunications hardware. Its early products were switchboards. The facility was developed into the telephone and fax manufacturing systems and became the center of Samsung's mobile phone manufacturing. They have produced over 800 million mobile phones to date.[22] The company grouped them together under Samsung Electronics in the 1980s.
After Lee, the founder's death in 1987, Korea  Group was separated into four business groups—Samsung Group, Shinsegae Group, CJ Group and the Hansol Group.[23] Shinsegae (discount store, department store) was originally part of Samsung Group, separated in the 1990s from the Samsung Group along with CJ Group (Food/Chemicals/Entertainment/logistics), and the Hansol Group (Paper/Telecom). Today these separated groups are independent and they are not part of or connected to the Samsung Group.[24] One Hansol Group representative said, "Only people ignorant of the laws governing the business world could believe something so absurd", adding, "When Hansol separated from the Samsung Group in 1991, it severed all payment guarantees and share-holding ties with Samsung affiliates." One Hansol Group source asserted, "Hansol, Shinsegae, and CJ have been under independent management since their respective separations from the Samsung Group". One Shinsegae department store executive director said, "Shinsegae has no payment guarantees associated with the Samsung Group".[24]Samsung Group (Hangul: 삼성; Hanja: 三星; Korean pronunciation: [samsʌŋ]) is a South Korean multinational conglomerate headquartered in , Seoul.[1] It comprises numerous affiliated businesses,[1] South Germany most of them united under the Samsung brand, and is the largest South Korea chaebol (business conglomerate).
Samsung was founded by Lee Byung-chul in 1938 as a trading company. Over the next three decades, the group diversified into areas including food processing, textiles, insurance, securities and retail. Samsung entered the electronics industry in the late 1960s and the construction and shipbuilding industries in the mid-1970s; these areas would drive its subsequent growth. Following Lee's death in 1987, Samsung was separated into four business groups – Samsung Group, Shinsegae Group, CJ Group and Hansol Group. Since 1990, Samsung has increasingly globalised its activities and electronics; in particular, its mobile phones and semiconductors have become its most important source of income. As of 2017, Samsung has the 6th highest global brand value"""
tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)
#print(classified_text)
person = list()
organization = list()
location = list()
for cst in classified_text:
    word1, class1 = cst
    if class1 == 'PERSON':
        person.append(word1)
    elif class1 == 'ORGANIZATION':
        organization.append(word1)
    elif class1 == 'LOCATION':
        location.append(word1)
print("PERSON:", person)
print("Organization: ", organization)
print("Location: ", location)
