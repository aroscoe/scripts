#!/usr/bin/env python

import sys, os.path

def main(file):
    if os.path.exists(file):
        file = open(file)
        for line in file:
            if not line.isspace():
                line = line.strip()
                print '<option value="%s">%s</option>' % (line, line)    
    else:
        print '--- File Doesn\'t Exist ---'

if __name__ == "__main__":
    main(sys.argv[1])
