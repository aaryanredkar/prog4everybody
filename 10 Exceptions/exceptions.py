

def main():
    try:
        fh = open('lines.txt')
        for line in fh: print(line.strip())
    except IOError as e:
        print ('could not open file:',e)
if __name__ == "__main__": main()


