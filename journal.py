#!/usr/bin/env python3
"""
A simple script to set up a daily journal file
"""
__author__ = "James Docherty"
__version__ = "1.0.0"
__license__ = "MIT"

import os.path
import datetime
import subprocess


def main():
    """ Main entry point of the app """
    # Set the location for the dj files
    dirname = '/Users/jmd/Dropbox/Documents/Writing/Journal/'

    # Choose the editor
    editor = 'Visual Studio Code'
    # editor = 'textEdit'
    # editor = 'iA Writer Classic'
    
    # create filename from date
    today_obj = datetime.date.today()
    filename = str(today_obj.year) + today_obj.strftime('%m') + today_obj.strftime('%d')+'.txt'

    filepath = dirname + filename
    
    print "Checking file..."
    print filepath
    # check if a file with today's date exists
    if os.path.isfile(filepath):
        print "Today's file already exists so opening it..."
        # if it does exist then open it
        subprocess.call(['open', '-a', editor, filepath]) # use the full app name when using the -a switch
    else:
        # if not, create one
        print "We need to create a new file"
        newfile = open(filepath, 'w+')
        newfile.write(str(today_obj) + '\n')
        newfile.close()
        subprocess.call(['open', '-a', editor, filepath])

if __name__ == "__main__":
    # This is executed when run from the command line
    main()
