from collections import Counter

# def list_has_duplicate_items( mylist ):
#     return len(mylist) > len(set(mylist))

def test_wordlength():
    dfile = open("dict", "r")
    for x in dfile:
        word = str(x.strip())
        assert len(word) >= 3, "Words in Dictionary must be greater or equal to 3. [" + word + '] failed this check'
    dfile.close()

def test_filelength():
    dfile = open("dict", "r")
    data = dfile.read().strip()
    #get the length of the data
    number_of_characters = len(data)
    assert number_of_characters <= 105, "Sum of words in Dictionary must not exceed 105 characters, i found " + str(number_of_characters)
    dfile.close()

def test_double_words():
    dfile = open("dict", "r")

    wordCount = Counter(dfile.read().split())

    doubleWords = []
    doubleWordsCounter = 0
    for i in wordCount:
        if wordCount[i] > 1:
            doubleWords.append(i)
            doubleWordsCounter += 1

    assert doubleWordsCounter == 0, "Words in Dictionary must occur only once. " + str(doubleWords) + " appears more"# + str(occurances) + " times"

    dfile.close()

if __name__ == "__main__":
    test_wordlength()
    test_filelength()
    test_double_words()
    print("All checks passed")


