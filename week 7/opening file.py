Python 2.7.10 (default, May 23 2015, 09:44:00) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Use words.txt as the file name
fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname =' words.txt'
fh = open(fname)
for line in fh :
    line = line.rstrip().upper()
    print line
