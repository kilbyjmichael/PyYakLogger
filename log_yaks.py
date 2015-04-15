#!/usr/bin/env python

'''Yik Yak Logger'''

import API as pyak
import sys
from datetime import datetime
import codecs

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
    
        yak_file = codecs.open(str(datetime.now().date()) + "_yak-log.txt", 'a', 'utf-8')
        
        old_yak = ["empty"]
        while True:
            get_yak = yakker.get_yaks()
            last_yak = get_yak[:-1]
            for yak in last_yak: # get last yak
                new_yak = yak.return_yak()
                yak_comments = yak.get_comments()
            if new_yak[0] != old_yak[0]: #check for duplicates
                try:
                    yak_file.write("<yak>\n") # open xml
                    for ele in new_yak:
                        yak_file.write(ele)
                        print(ele)
                        
                    for comment in yak_comments:
                        this_comment = comment.return_comment()
                        for ele in this_comment:
                            yak_file.write(ele)
                            print(ele)
                    yak_file.write("</yak>\n\n")
                    old_yak = new_yak
                    yak_file.flush()
                        
                except UnicodeEncodeError:
                    print("We had an error, and it is being handled.")
                    yak_file.write("<yak>\n") # open xml
                    for ele in new_yak:
                        new_ele = ele.encode(encoding="ascii", errors="replace")
                        new_ele = new_ele.decode(encoding="ascii", errors="replace")
                        yak_file.write(new_ele)
                        print(ele)
                        
                    for comment in yak_comments:
                        this_comment = comment.return_comment()
                        for ele in this_comment:
                            new_ele = ele.encode(encoding="ascii", errors="replace")
                            new_ele = new_ele.decode(encoding="ascii", errors="replace")
                            yak_file.write(new_ele)
                            print(ele)
                    yak_file.write("</yak>\n\n")
                    old_yak = new_yak
                    
if __name__ == "__main__": main()
