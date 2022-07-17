bk = open('bookmarks_7_16_22.html')
dup = open('dup.txt')

memdup = []

# read dups into memory
for x in dup:
    #print(x[:-1])
    memdup.append(x[:-1])


# check each link of bk for entry in dup 
for y in bk:
    ip = False
    for t in memdup:
        ip = (ip or (not (y.find(t) == -1)))
        if(y.find(t)>-1):  # only do this once
            memdup.remove(t)
    if (not ip):
        print(y)
# delete in both dup and omit bk line