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
    
    with open(str(datetime.now().date()) + "_yak-log.txt", 'a') as yak_file:
        old_yak = ["empty", "empty"]
        while True:
            get_yak = yakker.get_yaks()[:1]
            for yak in get_yak:
                new_yak = yak.return_yak()
            if new_yak[1] != old_yak[1]:
                for ele in new_yak:
                    yak_file.write(ele)
                    yak_file.flush()
                    old_yak = new_yak

if __name__ == "__main__": main()
