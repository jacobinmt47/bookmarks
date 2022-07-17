from html.parser import HTMLParser
class myparser(HTMLParser):
    myurllist =[]
    pairlist = []
    root = []
    dirflag = False
    rcount = 0
    dirtop = 0

    def handle_starttag(self,tag,attr):
        if(tag == "dl"):
            self.rcount = self.rcount+1
        if(tag == "h3"):
            self.dirflag = True

        if(tag == 'a'):
            if(not(attr[0] in self.myurllist)):
                self.myurllist.append(attr[0])

    #get bookmark name of url
    def handle_data(self ,data):
        if(self.dirflag == True):
            self.root.append(data)
            #print("handle dir:"+str(self.root))
            self.dirflag = False

        if(len(data)!= 0 and (len(self.myurllist)>0)):
            l = self.myurllist
            last = l.pop()
            t = data, last, str(self.root) 
            self.pairlist.append(t)
            pass

    # walk up a level
    def handle_endtag(self,tag):
        if(tag == "dl"):
           # print(self.rcount)
            self.rcount = self.rcount-1
            if(len(self.root)>0):
                #print(self.root.pop())
                self.root.pop()
    # write tags and bookmark stuff

    def cleanbk(self):
        for x in self.pairlist:
            print(x[2]+" ,name:"+x[0]+' ,url:'+x[1][1])


mp = myparser()
f = open('bookmarks.html')
mp.feed(f.read())
mp.cleanbk()