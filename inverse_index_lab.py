from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0,2)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    outlist = {}
    for in_doc,currdoc in enumerate(strlist):
        for currword in currdoc.split():
            if currword in outlist:
                outlist[currword] = outlist[currword] | {in_doc}
            else:
                outlist[currword] = {in_doc}
    
    return outlist

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    outlist = set()
    for x in query:
        if x in inverseIndex:
            outlist = outlist | inverseIndex[x]
    
    return outlist

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    outlist = set()
    f_first = 1
    for x in query:
        if x in inverseIndex:
            if f_first == 1:
                outlist = inverseIndex[x]
                f_first = 0
            else:
                outlist = outlist & inverseIndex[x]
    
    return outlist
