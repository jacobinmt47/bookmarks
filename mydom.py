from xml.dom.minidom import getDOMImplementation

#newdoc is the root document
#url is the web address
#site is the name given to the url, it's what the user see
def makeList(newdoc,url,site):
    top_element = newdoc.documentElement
    li = newdoc.createElement("li")
    alink = newdoc.createElement("a")
    top_element.appendChild(li)
    text = newdoc.createTextNode(str(site))
    a1 = newdoc.createAttribute("href")
    a1.value = str(url)
    alink.setAttributeNode(a1)
    alink.appendChild(text)
    li.appendChild(alink)



impl = getDOMImplementation()
newdoc = impl.createDocument(None,"ul",None)
 
makeList(newdoc,"http://google.com","google")
makeList(newdoc,"http://bing.com","bing")

print(newdoc.documentElement.toprettyxml())