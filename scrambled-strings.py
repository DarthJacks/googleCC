import sys, getopt
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# def checkWordSorted(inputWord, dictWord):
#   if sorted(inputWord) == sorted(dictWord):
#     return True
#   else:
#     return False

inputfile = "1"
outputfile = "2"


def logOut(logText):
  abc = 1
  print(logText)

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
      logOut("Checking " + word + ", length " + str(lenword))
      lenInput = len(inputf)
      
      for step in range(lenInput-lenword+1):
        endingStep = step+lenword
        chekDictionary = inputf[step:endingStep]
        if chekDictionary == word:
          logOut(word + " occurs in its original form, possition " + str(step) )
          unScrambledOccurances += 1
        elif sorted(word) == sorted(chekDictionary) and word[0] == chekDictionary[0] and word[lenword-1] == chekDictionary[lenword - 1]:
          logOut(word + " occurs in its scrambled form as " + chekDictionary + ", possition " + str(step))
          scrambledOccurances += 1
          
        
      logOut("Scrambled Occurances: " + str(scrambledOccurances) + ", Unscrambled Occurances: " + str(unScrambledOccurances) + '\n----------------')

      if (scrambledOccurances + unScrambledOccurances > 0):
        wordHits += 1

    print("Case #" + str(caseNum) + ": " + str(wordHits))
    dfile.close()

    caseNum += 1

  inputfile.close()

def mainArgs(argv):
  inputfile = ""
  outputfile = ""
  try:
    opts, args = getopt.getopt(argv,"hi:o",["ifile=","dfile="])
  except getopt.GetoptError:
    print ("test.py -input <inputfile> -dictionary <dictionaryfile>")
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print ("test.py -input <inputfile> -dictionary <dictionaryfile>")
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-o", "--dfile"):
      outputfile = arg

  print ("Input file is " + inputfile)
  print ("Output file is " + outputfile)

if __name__ == "__main__":
  #mainArgs(sys.argv[1:])
  # logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
  # logging.debug('This message should go to the log file')
  # logging.info('So should this')
  # logging.warning('And this, too')
  # logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
  runMain("dict", "input")

