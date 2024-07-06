import csv
from curses.ascii import isalpha
import sys
import os

def process_file(file):
    """
    Process the given file and write the output to "myOutFile.txt".

    Args:
        file (str): The path to the input file.

    Returns:
        None
    """
    f = open(str(file))

    outF = open("myOutFile.txt", "w")

    for i, x in enumerate(f):
        if(len(x)<3): 
            continue
        elif(x[2]==':'):
            y = x.split(':')
            y= y[0:3]
            y[2]= y[2][:-11]
            if len(y) <= 1:
                continue
            s= int(y[0])
            if(s==0):
                s=""
            else:
                s= str(s)+":"
            a= int(y[1])
            f= str(s+str(a)+":"+y[2])
            outF.write(f)
            outF.write("\n")
        elif(x[0].isalpha() or x[1].isalpha()):
            outF.write(x)

    f.close()
    outF.close()
