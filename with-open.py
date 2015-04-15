with open(str(datetime.now().date()) + "_yak-log.txt", 'w') as yak_file:
    # read yaks!
    while True:
        new_yak = yak.return_yak(yakker.get_yaks()[:1])        # get new yak off stack
        time.sleep(5)                           # wait for stack to update remotely
        old_yak = new_yak                       # old = new
        new_yak = yak.return_yak(yakker.get_yaks()[:1])        # get new new yak
        
        if new_yak is not old_yak:              # if new new is not old
            for ele in

old_yak = []
while True:
    new_yak = yak.return_yak(yakker.get_yaks()[:1])
    if new_yak[2] != old_yak[2]:
        for ele in new_yak:
            print(ele)
            # yak_file.flush()
            old_yak = new_yak