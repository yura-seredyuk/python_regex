# RegEX
# - words
# - letters
# - specisl commands need to use ecran cymbol \
#  - \d  - one digit
#  - \D  - oll without digits
#  -  . any simbol
#  - \w  - any digit or letter
#  - \W  - any symbol but not digit or letter
#  - \s - breakespace
#  - \S - all but not breakespace
#  - \w+ - words or numbers
#  - + - 1 and more
#  - ? - 0 or 1
#  - * - 0 or more
#  - ^ - begin of line
#  - $ - end of loine 
#  - [] - group
#  - {n} - n count repeat
#  - {n, m} - from n to m count repeat

TEST_STRING = """
Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, \
and first released it in 1991 as Python 0.9.0. [32] Python 2.0 was released in 2000 Guido and introduced new features, \
such as list comprehensions and a garbage collection system using reference counting. Guido Python 3.0 was released in 2008 \
and was a major revision of the language that is not completely backward-compatible. Python 2 was discontinued with version \
2.7.18 in 2020. Guido

email@invalid
em@ail@invalid.com
email@valid.com
email@valid.ua
email@valid.ru
email@valid.mil

email@@valid.com

127.0.0.1

https://regex101.com
https://regex101.com/r/GuSlli/1/
http://regex101.com/r/GuSlli/1/
https://www.regex101.com/r/GuSlli/1/
"""

import re

# pattern = re.compile(r'(https?://)(www\.)?([a-zA-Z0-9-[\.\w+]+)([\w/]+)')
# # matches = pattern.findall(TEST_STRING)
# matches = pattern.finditer(TEST_STRING)

# for match in matches:
#     print(match.group(0))
#     print(match.group(1))
#     print(match.group(2))
#     print(match.group(3))
#     print(match.group(4))

# pattern = re.compile(r'([a-zA-Z0-9-_\*\.]+)@([a-zA-Z0-9-]+)(\.[a-zA-Z0-9]+)+')
# matches = pattern.finditer(TEST_STRING)

# for match in matches:
#     print(match.group(0))

TEST_TEXT = "Python Guido van Rossum began working on Python in the late 1980s, as Python a successor to the ABC Python programming language, \
and first released it in 1991 as Python 0.9.0."

# pattern = re.compile(r'Python')
# matches = pattern.finditer(TEST_STRING)
# matches = pattern.findall(TEST_STRING)

# matches = pattern.search(TEST_TEXT)
# matches = pattern.match(TEST_TEXT)
# matches = re.search(r'Python',TEST_TEXT)
# print(matches)
# import random

# words = ['C++', 'CSS', 'HTML']
# for i in range(len(matches)):
#     TEST_TEXT = pattern.sub(random.choice(words), TEST_TEXT, 1)



# rez = pattern.split(TEST_TEXT)

# print(TEST_TEXT)

def verifyPassword(password:str):
    strong_pattern = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z])(?=.*[*.!@$%^&(){}[\]:;<>,.?\/~_+-=|\\]).{8,}$')
    middle_pattern = re.compile(r'((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{6,}))|((?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])(?=.{8,}))')

    if strong_pattern.search(password):
        return 'Strong password'
    elif middle_pattern.search(password):
        return 'Middle password'
    elif len(password)>= 8:
        return 'Light password'
    return 'Incorrect password'


print(verifyPassword('1111'))
print(verifyPassword('qwertyui'))
print(verifyPassword('Testing193'))
print(verifyPassword('Testing193$$'))



