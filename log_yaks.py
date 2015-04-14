#!/usr/bin/env python

'''Yik Yak Logger'''

import API as pyak
import sys
from datetime import datetime

def main():
    # set location/user for the API
    coord_location = pyak.Location(40.5115765, -88.9933131) # ISU
    user_ID = "CA44EC42-D50A-4B52-AAC2-D815934AD23A"
    # make a yakker
    yakker = pyak.Yakker(user_ID, coord_location, False)
    
    # check everything
    print("User ID: ", yakker.id, "\n")
    print("Connecting to Yik Yak...\n")
    internet_on = True
    try:
        print("Yakarma Level: ",yakker.get_yakarma(), "\n")
    except:
        print("Error: Not connected to the Internet\n")
        internet_on = False
    if internet_on:
        print("Reading Yaks... -->")
    
        # read yaks!
        yak_list = [] # objects
        while True:
            yak_list = yakker.get_yaks()
            show(yak_list)

def show(yaklist):
    yakNum = 1
    sys.stdout = open(str(datetime.now().date()) + "_yak-log.txt", 'w')
    for yak in yaklist:
        # line between yaks
        print ("_" * 93)
        # show yak
        print (yakNum)
        yak.print_yak()
        
        commentNum = 1
        # comments header
        comments = yak.get_comments()
        print ("\n\t\tComments:", end='')
        # number of comments
        print (len(comments))
        
        # print all comments separated by dashes
        for comment in comments:
            print ("\t   {0:>4}".format(commentNum), end=' ')
            print ("-" * 77)
            comment.print_comment()
            commentNum += 1
        yakNum += 1
        sys.stdout.flush()

if __name__ == "__main__": main()
