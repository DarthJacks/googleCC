import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def checkWordSorted(inputWord, dictWord):
  if sorted(inputWord) == sorted(dictWord):
    return True
  else:
    return False


def runMain():

  caseNum = 1
  inputfile = open("input")

  for inputf in inputfile:
    inputf = str(inputf)
    wordHits = 0

    dfile = open("dict", "r")
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


if __name__ == "__main__":
    runMain()

