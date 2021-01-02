# coding=utf-8
from collections import Counter
import sys, getopt
import traceback


# def list_has_duplicate_items( mylist ):
#     return len(mylist) > len(set(mylist))
errors = 0

def test_wordlength(dictionary_filename):
    wordlength_errors = 0
    dfile = open(dictionary_filename, "r")
    for x in dfile:
        word = str(x.strip())
        try:
            assert len(word) >= 3, "Words in Dictionary must be greater or equal to 3. [" + word + '] failed this check'
        except AssertionError:
            print("AssertionError: Words in Dictionary must be greater or equal to 3. [" + word + '] failed this check')
            wordlength_errors += 1
    dfile.close()
    return wordlength_errors

def test_filelength(dictionary_filename):
    filelength_errors = 0
    dfile = open(dictionary_filename, "r")
    data = dfile.read().strip()
    #get the length of the data
    number_of_characters = len(data)
    try:
        assert number_of_characters <= 105, "Sum of words in Dictionary must not exceed 105 characters, Found " + str(number_of_characters)
    except AssertionError:
        print("AssertionError: Sum of words in Dictionary must not exceed 105 characters, Found " + str(number_of_characters))
        filelength_errors += 1
    dfile.close()
    return filelength_errors


def test_double_words(dictionary_filename):
    double_word_errors = 0
    dfile = open(dictionary_filename, "r")

    wordCount = Counter(dfile.read().split())

    doubleWords = []
    doubleWordsCounter = 0
    for i in wordCount:
        if wordCount[i] > 1:
            doubleWords.append(i)
            doubleWordsCounter += wordCount[i]
    try:
        assert doubleWordsCounter == 0, "Words in Dictionary must occur only once. " + str(doubleWords) + " appears more"# + str(occurances) + " times"
    except AssertionError:
        print("AssertionError: Words in Dictionary must occur only once. " + str(doubleWords) + " appears more, " + str(doubleWordsCounter))
        double_word_errors += 1

    dfile.close()
    return double_word_errors


if __name__ == "__main__":
    dictionary_filename = "dict"
    verbose = False


    try:
        options, remainder = getopt.getopt(sys.argv[1:], "d:v", ["dictionary=", 
                                                          "verbose",
                                                          ])
        for opt, arg in options:
            if opt in ("-d", "--dictionary"):
                dictionary_filename = arg
            elif opt in ("-v", "--verbose"):
                verbose = True
    except getopt.GetoptError:
        print ("test.py --dictionary <dictionaryfile> -v verbose ")
        sys.exit(2)

    if not (test_wordlength(dictionary_filename) + test_filelength(dictionary_filename) + test_double_words(dictionary_filename)):
        print("All checks passed")
    else:
        sys.exit(2)
    

