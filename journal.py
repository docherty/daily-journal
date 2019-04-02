#!/usr/bin/env python3
"""
A simple script to set up a daily journal file
"""
__author__ = "James Docherty"
__version__ = "0.1.0"
__license__ = "MIT"

import os.path
import datetime

import subprocess


def main():
    """ Main entry point of the app """
    dirname = '/Users/jmd/Dropbox/Documents/Writing/Journal/'

    # create filename from date
    today_obj = datetime.date.today()
    filename = str(today_obj.year) + today_obj.strftime('%m') + today_obj.strftime('%d')+'.txt'
    # filename = '20190401.txt'

    filepath = dirname + filename
    # editor = 'textEdit'
    # editor = 'iA Writer Classic'
    editor = 'Visual Studio Code'

    print "Checking file..."
    print filepath
    # check if a file with today's date exists
    if os.path.isfile(filepath):
        print "Today's file already exists so opening it..."
        # if it does exist then open it
        subprocess.call(['open', '-a', editor, filepath])
    # if not, create one
    else:
        print "We need to create a new file"
        newfile = open(filepath, 'w+')
        newfile.write(str(today_obj) + '\n')
        newfile.close()
        subprocess.call(['open', '-a', editor, filepath])

if __name__ == "__main__":
    # This is executed when run from the command line
    main()
