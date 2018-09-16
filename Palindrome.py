"""
Palindrome.py - A simple palindrome validator script
User enters a word, phrase, or sentence and the program tests if it is a palindrome.
Differences in capitalization and spacing are supported.
User can specify if results are to be reported in boolean form.
"""

import argparse
parser = argparse.ArgumentParser()
#   User defined input parameter called -i or --input
parser.add_argument('-i', '--input', action="store", dest="palin",
                    default="kayak", help="Text to check")
#   User defined input parameter called -b or -boolean
#   Defaults to false unless set by user
parser.add_argument('-b', '--boolean', action="store_true", dest="bool",
                    default="False", help="Report result in boolean form")
options = parser.parse_args()
test = options.palin
#   Change input to lowercase
test = test.lower()
#   Remove spaces in input
test = test.replace(" ", "")

#   Reverse input
reversed_test = test[::-1]
if test == reversed_test:
    if options.bool == 1:
        print(options.bool)
    else:
        print("The input '" + options.palin + "' is a palindrome")
else:
    if options.bool == 1:
        print("False")
    else:
        print("The input '" + options.palin + "' is not a palindrome")

# END file Palindrome.py
