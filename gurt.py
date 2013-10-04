#!/usr/bin/env python

import sys
import os
import re

#
# This program reproduces (a sterile version of) itself, and then executes it.
#
# A bittersweet parody of "terminator technology" aka GURT(Genetic use restriction technology)
#

def main():
    ownName=os.path.basename(sys.argv[0])
    otherName='gurt2.py'
    
    if(ownName=='gurt2.py'):
        otherName='gurt.py'

    print "My name is: "+ownName
    print "The other name is: "+otherName

    file = open(ownName, "r")
    
    text=""
    i=0
    for line in file:
        if re.search("os.system", line): #(*) to ignore this line
            i=i+1            
            if(i>2):                     # 2 is 1(*)+ 1(**)                
                line=line.replace("os.system(otherName)","#os.system(otherName)") #(**) and this one
                line=line.replace("will be", "has been")
                print "terminated:"+line
        text+=line

    file.close()

                
    otherFile= open(otherName,'w')
    otherFile.write(text)
    otherFile.close()
    
    os.system(otherName) #This gene will be silenced
    exit(0)
  
if __name__ == '__main__':
    main()
    
