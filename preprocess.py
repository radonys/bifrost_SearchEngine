import os
import importlib
import argparse
import sys
import collections
import json

import indexing
import text_extract as TE
import summarisation

def main(args):

    words = collections.defaultdict(dict) #Stores words, documents containing them and positional indices.
    words_tfidf = collections.defaultdict(dict) #Stores TF, IDF & TF-IDF.
    text = dict()
    filecount = 0

    #If no data is given as input.
    if args.data_dir==None:
        sys.exit("No Data Available")

    #Text documents are given.
    elif args.data_dir!=None:
        file = open("data/path.json",'w')
        json.dump(args.data_dir,file)
        file.close()
        filecount = indexing.index(words,args.data_dir)
        indexing.datasave(words,3)
        indexing.tfidf(words,words_tfidf,filecount)
        indexing.datasave(words_tfidf,1)

    if indexing.is_empty(text)==True:
        
        for folder,subfolders,files in os.walk(args.data_dir):
            for filename in files:
                TE.summarize_text(os.path.join(os.path.abspath(folder),filename),text)
        
        indexing.datasave(text,2)
    
    #summarisation.summarize()
    
def parse_arguments(argv):
    
    parser = argparse.ArgumentParser()

    parser.add_argument('--data_dir', type=str, help='Path to the data directory', default=None)

    return parser.parse_args(argv)

if __name__ == '__main__':
	
	main(parse_arguments(sys.argv[1:]))