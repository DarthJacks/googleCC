# coding=utf-8
import sys, getopt
import logging
import test
logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

# def checkWordSorted(inputWord, dictWord):
#   if sorted(inputWord) == sorted(dictWord):
#     return True
#   else:
#     return False

def logOut(logText):
  if verbose:
    logging.info(logText)


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
      logOut("Checking [" + word + "], length " + str(lenword))
      lenInput = len(inputf)
      
      for step in range(lenInput-lenword+1):
        endingStep = step+lenword
        chekDictionary = inputf[step:endingStep]
        if chekDictionary == word:
          logOut("[" + word + "] occurs in its original form, possition " + str(step) )
          unScrambledOccurances += 1
        elif sorted(word) == sorted(chekDictionary) and word[0] == chekDictionary[0] and word[lenword-1] == chekDictionary[lenword - 1]:
          logOut("[" + word + "] occurs in its scrambled form as " + chekDictionary + ", possition " + str(step))
          scrambledOccurances += 1
          
        
      logOut("Scrambled Occurances: " + str(scrambledOccurances) + ", Unscrambled Occurances: " + str(unScrambledOccurances) + "\n----------------")

      if (scrambledOccurances + unScrambledOccurances > 0):
        wordHits += 1

    print("Case #" + str(caseNum) + ": " + str(wordHits))
    logOut("------------------------------------------------------")
    dfile.close()

    caseNum += 1

  inputfile.close()


if __name__ == "__main__":
  dictionary_filename = "dict"
  input_filename = "input"
  verbose = False
  
  try:
    options, remainder = getopt.getopt(sys.argv[1:], "d:i:v", ["dictionary=", 
                                                          "input=",
                                                          "verbose",
                                                          ])
    for opt, arg in options:
      if opt in ("-d", "--dictionary"):
          dictionary_filename = arg
      elif opt in ("-i", "--input"):
          input_filename = arg
      elif opt in ("-v", "--verbose"):
          verbose = True
  except getopt.GetoptError:
    print ("scrambled-strings.py --input <inputfile> --dictionary <dictionaryfile> -v verbose ")
    sys.exit(2)

  if not (test.test_wordlength(dictionary_filename) + test.test_filelength(dictionary_filename) + test.test_double_words(dictionary_filename)):
    runMain(dictionary_filename, input_filename)
  else:
    print("Unit Tests failed, Please fix and re-run")
   




  # logging.basicConfig(filename="example.log", encoding="utf-8", level=logging.DEBUG)
  # logging.debug("This message should go to the log file")
  # logging.info("")
  # logging.warning("")
  # logging.error("")


