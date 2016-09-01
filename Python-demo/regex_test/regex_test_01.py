'''
Created on 2016. 8. 29.

@author: YonghoonJi
'''

''' 
Perl-like regular expressions

a, X, 9, < -- ordinary characters just match themselves exactly.
. (a period) -- matches any single character except newline '\n'
\w -- matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_].
\W -- matches any non-word character.
\b -- boundary between word and non-word
\s -- matches a single whitespace character -- space, newline, return, tab
\S -- matches any non-whitespace character.
\t, \n, \r -- tab, newline, return
\d -- decimal digit [0-9]
^ = matches start of the string
$ = match the end of the string
\ -- inhibit the "specialness" of a character. 

Compilation flag
A (ASCII) : Makes several escapes like \w, \b, \s and \d match only on ASCII characters with the respective property.
S (DOTALL) : Make . match any character, including newlines
I (IGNORECASE) : Do case-insensitive matches
L (LOCALIE) : Do a locale-aware match
M (MULTILINE) : Multi-line matching, affecting ^ and $
X (VERBOSE) : Enable verbose REs, which can be organized more cleanly and understandably
'''


''' test match : match only at the beginning of the string '''
import re

line = 'cats are smarter than dogs'
matchObject = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObject:
    print('matchObj.group():', matchObject.group())
    print('matchObj.group(1):', matchObject.group(1))
    print('matchObj.group(2):', matchObject.group(2))
else:
    print("No match!!")


''' test search : checks for a match anywhere in the string'''
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObject:
    print('matchObj.group():', matchObject.group())
    print('matchObj.group(1):', matchObject.group(1))
    print('matchObj.group(2):', matchObject.group(2))
else:
    print("Nothing found!!")


''' test match and search '''
matchObject = re.match(r'dogs', line, re.M|re.I)

if matchObject:
    print("match --> matchObj.group():", matchObject.group())
else:
    print("no match")
    
matchObject = re.search(r'dogs', line, re.M|re.I)

if searchObj:
    print("search --> searchObj.group():", searchObj.group())
else:
    print("nothing found")
    
    
''' search and replace '''
phone = '2004-959-559 # This is Phone Number' 
num = re.sub(r'\s#.*$', '', phone)
print('Phone num:', num)
# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print('Phone num:', num)

text = "Python and Python is lang"
matchedText = re.match(r'Python(?=!)', text, re.I)
print(matchedText)
    