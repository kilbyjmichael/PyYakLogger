def return_yak(self):
    output = []
	try:
        output.append("<yak>")
        if self.handle is not None:
           output.append("<handle>%s</handle>" % self.handle)
        output.append("<message>%s</message>" % self.message)
        output.append("<likes>%s</likes>" % self.likes)
        output.append("<time>%s</time>" % self.time)
        output.append("<lat>%s</lat>" % self.latitude)
        output.append("<long>%s</long>" % self.longitude)
        output.append("</yak>")
    except UnicodeEncodeError:
        self.message = re.sub('[^\x00-\x7F]', '',self.message)
        
        output.append("<yak>")
        if self.handle is not None:
           output.append("<handle>%s</handle>" % self.handle)
        output.append("<message>%s</message>" % self.message)
        output.append("<likes>%s</likes>" % self.likes)
        output.append("<time>%s</time>" % self.time)
        output.append("<lat>%s</lat>" % self.latitude)
        output.append("<long>%s</long>" % self.longitude)
        output.append("</yak>")
    return output
    
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