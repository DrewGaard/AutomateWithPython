import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
resume = 'My name is Bob and my phone number is 555-555-5555 please contact me with questions.'
print(phoneRegex.search(resume))
print(phoneRegex.findall(resume))

vowelRegex = re.compile(r'[aeiouAEIOU]') # r'(a|e|i|o|u)'
print(vowelRegex.findall('The quick brown fox jumped over the'))
