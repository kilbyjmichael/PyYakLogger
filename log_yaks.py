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
    
    with open(str(datetime.now().date()) + "_yak-log.txt", 'w') as yak_file:
        # read yaks!
        yak_list = [] # objects
        while True: # sched
            new_yak = yakker.get_yaks()[:1]
            old_yak = yakker.get_yaks()[1:2]
            # check for repeat
            if old_yak == new_yak:
                print("this works")
            # only get first yak off list
            for yak in new_yak:
                xml_yak = yak.return_yak()
                for ele in xml_yak:
                    print(ele)
                yak_file.flush()

if __name__ == "__main__": main()
