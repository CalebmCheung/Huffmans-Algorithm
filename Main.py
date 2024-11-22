###################################
# Author: Caleb Cheung
# Decs: Main class responsible for reading in file and building tree
#
###################################

def main():
    print("hello world")
    fileName = "test1.txt"
    frequencyTable = {}

    with open(fileName) as f:
        while True:
            c = f.read(1)
            if not c:
                print("End of file")
                break
            # check if char is already in dictionary
            if c in frequencyTable:
                frequencyTable[c] += 1
            else:
                frequencyTable[c] = 1
        
    print(frequencyTable)

main()