#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Changing Word Script
"""

import sqlite3 as sql
import codecs
import os, glob

def fetchWord(word):
    """
    Fetch match word in database
    using: fetch(yourWord)
    """
    data = sql.connect("data.db")
    cursor = data.cursor()
    fetch = cursor.execute("SELECT * FROM Text WHERE Thai = (?)", (word,))
    if fetch:
        for row in fetch:
            return row[1]
    else:
        return False
    data.close()

def changeText(text):
    """
    Change one text
    using: changeText(your_text)
    """
    #three step searching---------------------------------------------------------------------------------
    startThreeWord = 0
    endThreeWord = 3
    for _ in xrange(len(text) - len(text) % 3):
        if fetchWord(text[startThreeWord:endThreeWord]):
            text = text[:startThreeWord] + fetchWord(text[startThreeWord:endThreeWord]) + text[endThreeWord:]
        startThreeWord += 1
        endThreeWord += 1
    #------------------------------------------------------------------------------------------------------

    #two step searching--------------------------------------------------------------------------- 
    startTwoWord = 0
    endTwoWord = 2
    for _ in xrange(totalWord):
        if fetchWord(text[startTwoWord:endTwoWord]):
            text = text[:startTwoWord] + fetchWord(text[startTwoWord:endTwoWord]) + text[endTwoWord:]
        startTwoWord += 1
        endTwoWord += 1
    #----------------------------------------------------------------------------------------------
    return text

def changeFile(f):
    """
    Change word in file
    using: changeFont(yourFiles)
    """
    path = "newScene"
    if not os.path.exists(path): #create new folder if not exist
        os.makedirs(path)
        
    oldFile = codecs.open(f, "r", "utf-8")   #file for reading
    newFile = codecs.open("newScene/" + f, "w", "utf-8")  #file for changing
    countLine = 0
    completeLine = 0
    for count in oldFile:
        if count[0:2] != "//":
            countLine += 1
    print "Find %d line in total." % countLine
    print "starting to change all text..."
    oldFile = codecs.open(f, "r", "utf-8")
    
    for row in oldFile:
        if row[0:2] != "//":
            totalWord = len(row)
            finalWordThree = totalWord % 3
            
            #three step searching---------------------------------------------------------------------------------
            startWordThree = 0
            endWordThree = 3
            for _ in xrange(totalWord - finalWordThree):
                if fetchWord(row[startWordThree:endWordThree]):
                    row = row[:startWordThree] + fetchWord(row[startWordThree:endWordThree]) + row[endWordThree:]
                startWordThree += 1
                endWordThree += 1
            #------------------------------------------------------------------------------------------------------

            #two step searching--------------------------------------------------------------------------- 
            startTwoWord = 0
            endTwoWord = 2
            for _ in xrange(totalWord):
                if fetchWord(row[startTwoWord:endTwoWord]):
                    row = row[:startTwoWord] + fetchWord(row[startTwoWord:endTwoWord]) + row[endTwoWord:]
                startTwoWord += 1
                endTwoWord += 1
            #----------------------------------------------------------------------------------------------

            completeLine += 1
            print "complete line:", completeLine, "/", countLine
            newFile.write(row)
        else:
            newFile.write(row)
    print "Finish!"
    odlFile.close()
    newFile.close()

def changeAll():
    """
    Change all files in current directory
    """
    for files in glob.glob("*.txt"):
        changeFile(files)

if __name__ == "__main__":
    changeAll()