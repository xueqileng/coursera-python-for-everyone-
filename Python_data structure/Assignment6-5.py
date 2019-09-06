# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
# Convert the extracted value to a floating point number and print it out.

#----------DesiredOutput--------
#0.8475

#-----------SourceCode----------
#text = "X-DSPAM-Confidence:    0.8475";

#-------------Answer------------
text = "X-DSPAM-Confidence:    0.8475";
startPos=text.find(':')
num=text[startPos+1:len(text)]
print(float(num))