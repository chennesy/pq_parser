# encoding: utf-8
## Adapted from
## Module to parse Proquest full-text newspaper files
## Tested with a sample of Ethnic Newswatch files
## Alex Hanna (alex.hanna@gmail.com)

import os
import re
import sys

SEP = "____________________________________________________________"

def parseProquest(filename):
    text = open(filename, 'r').read()

    print(filename)

    ## Split by Proquest header separator (SEP)
    docs = []
    ids  = []
    for i, d in enumerate(re.split(SEP, text)):
        d = d.strip()
        docs.append(d)
        if re.match(r'Document \d+ of \d+', d):
            ids.append(i)
        file = open("out/" + str(i)+ ".txt","w") 
        file.write(docs[i]) 
        file.close() 
        
parseProquest("ProQuestDocuments-2019-07-14.txt")