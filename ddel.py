from html.parser import HTMLParser
class myparser(HTMLParser):
    myurllist =[]
    dirflag = False

    #print duplicate urls
    def handle_starttag(self,tag,attr):
        if(tag == 'a'):
            if(not((attr[0]) in self.myurllist)):
                self.myurllist.append(attr[0])
                # print("append: "+str(attr[0]))
            else:
                print(str(attr[0][1]))

    

mp = myparser()
f = open('bookmarks_7_16_22.html')
mp.feed(f.read())