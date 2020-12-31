# googleCC
Count how many of the words from a dictionary appear as substrings in a long string of
characters either in their original form or in their scrambled form. The scrambled form of the
dictionary word must adhere to the following rule: the first and last letter must be maintained
while the middle characters can be reorganised.

The scrambled or original form of the dictionary word may appear multiple times but we only
count it once since we only need to know whether it shows up at least once.

For example, if we had the word this in the dictionary, the possible valid words which would be
counted are this (original version) and tihs (scrambled version). tsih, siht and other variations
are not valid since they do not start with t and end with s. Also, tis, tiss, and thiss are not
scrambled forms, because they are not reorderings of the original set of letters.


Input consist of:
1. a dictionary file, where each line comprises one dictionary word from which you can
create your dictionary. E.g. “and”, “bath”, etc, but note the dictionary words do not need
to be real words.
2. an input file that contains a list of long strings, each on a newline, that you will need to
use to search for your dictionary words. E.g. “btahand”

Output
Treating each line of the input file as one search string, your program should output a line Case
#x: y per input file string, where x is the line number (starting from 1) and y is the number of
words from the dictionary that appear (in their original or scrambled form) as substrings of the
given string.

Limits
● No two words in the dictionary are the same.
● Each word in the dictionary is between 2 and 105 letters long, inclusive.
● The sum of lengths of all words in the dictionary does not exceed 105.