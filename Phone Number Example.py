import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False # not phone number-sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # no first 3 digits
    if text[7] != '-':
        return False # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # missing last 4 digits
    return True

print(isPhoneNumber('415-555-1234'))
print(isPhoneNumber('Hello'))

message = 'Call 415-555-1234 for more information!'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # so much better to use regex
mo = phoneNumRegex.search(message)
print(mo.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo2 = batRegex.search('Batman sat in the Batmobile looking up at the bats flying aroung the Batcopter')
print(mo2.group())
