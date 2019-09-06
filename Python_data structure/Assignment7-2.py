#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

#----------DesiredOutput--------
#Average spam confidence: 0.750718518519

#-----------SourceCode----------
# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# for line in fh:
#    if not line.startswith("X-DSPAM-Confidence:") : continue
#    print(line)
# print("Done")

#-------------Answer------------
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
value = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    pos=line.find(':')
    num=line[pos+1:len(line)]
    count=count+1
    value=value+float(num)
print("Average spam confidence:",value/count)


fname = input("Enter file name: ")
fh = open(fname)
count = 0
value = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count=count+1
        find=line.find(":")
        extracting=line[find+1:len(line)]
        value=value+float(extracting)
print(value/count)
