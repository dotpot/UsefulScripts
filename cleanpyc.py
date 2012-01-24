__author__ = 'Lukas Salkauskas'
import os, sys

def cleanpyc(dir):
    cmdQuery = 'find %s -name "*.pyc" -print' % dir
    count = 0
    for file in os.popen(cmdQuery).readlines():
        count += 1
        print str(file[:-1])
        os.remove(str(file[:-1]))

    print "Removed %d .pyc files" % count

if __name__ == "__main__":
    cleanpyc(".")