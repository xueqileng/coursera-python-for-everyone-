#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

#----------DesiredOutput--------
#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1

#-----------SourceCode----------

#-------------Answer------------
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours=dict()
for line in handle:
    if line.startswith("From") and not line.startswith("From:"):
        lst=line.split()
        time=lst[5]
        hour=time.split(':')
        hours[hour[0]]=hours.get(hour[0],0)+1

outputLst=list()
for hour,count in hours.items():
    outputLst.append((hour,count))

outputLst.sort()
for var in outputLst:
    print(var[0],var[1])

#mycode
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=dict()
for line in handle:
    line=line.rstrip()
    if line.startswith("From") and not line.startswith("From:"):
        word=line.split()
        word=word[5]
        newword=word.split(":")[0]
        count[newword]=count.get(newword,0)+1
count=sorted(count.items())
for v,k in count:
    print(v,k)
