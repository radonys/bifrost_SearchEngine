import os
import importlib
import sys
import collections

import text_extract as TE

def index(words,filepath):

    for folder,subfolders,files in os.walk(filepath):
        
        for filename in files:
    
            text_data = TE.extract(os.path.join(os.path.abspath(folder),filename))

            if text_data != None:
                
                processed = TE.textprocess(text_data)

                for word in processed:
                    
                    term = word
                    document = os.path.join(os.path.abspath(folder),filename)
                    positions = [index for index, value in enumerate(processed) if value == term]
                    words[term][document] = positions