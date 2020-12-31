import sys
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# def checkWordSorted(inputWord, dictWord):
#   if sorted(inputWord) == sorted(dictWord):
#     return True
#   else:
#     return False


def runMain(dictionaryFile, inputFile):

  caseNum = 1
  
  inputfile = open(inputFile)
  #loop cases in input file
  for inputf in inputfile:
    inputf = str(inputf.strip())
    wordHits = 0

    dfile = open(dictionaryFile, "r")
    #loop dictionary words
    for x in dfile:
      unScrambledOccurances = 0
      scrambledOccurances = 0
      word = x.strip()
      lenword = len(word)
      print("Checking " + word + ", length " + str(lenword))
      lenInput = len(inputf)
      
      for step in range(lenInput-lenword+1):
        endingStep = step+lenword
        chekDictionary = inputf[step:endingStep]
        if chekDictionary == word:
          print(word + " occurs in its original form, possition " + str(step) )
          unScrambledOccurances += 1
        elif sorted(word) == sorted(chekDictionary):
          print(word + " occurs in its scrambled form as " + chekDictionary + ", possition " + str(step))
          scrambledOccurances += 1
        
      print("Scrambled Occurances: " + str(scrambledOccurances) + ", Unscrambled Occurances: " + str(unScrambledOccurances) + '\n----------------')

      if (scrambledOccurances + unScrambledOccurances > 0):
        wordHits += 1

    print("Case #" + str(caseNum) + ": " + str(wordHits) + "\n")
    dfile.close()

    caseNum += 1

  inputfile.close()

# def mainArgs(argv):
#    inputfile = ""
#    outputfile = ""
#    try:
#       try:
#       opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
#    except getopt.GetoptError:
#       print 'test.py -i <inputfile> -o <outputfile>'
#       sys.exit(2)
#    for opt, arg in opts:
#       if opt == '-h':
#          print 'test.py -i <inputfile> -o <outputfile>'
#          sys.exit()
#       elif opt in ("-i", "--ifile"):
#          inputfile = arg
#       elif opt in ("-o", "--ofile"):
#          outputfile = arg
#    print 'Input file is "', inputfile
#    print 'Output file is "', outputfile

  # def getArgs()
  #   print 'Number of arguments:', len(sys.argv), 'arguments.'
  #   print 'Argument List:', str(sys.argv)


if __name__ == "__main__":
  # print 'Number of arguments:', len(sys.argv), 'arguments.'
  # print 'Argument List:', str(sys.argv)
  # mainArgs(sys.argv[1:])
  runMain("dict", "input")

