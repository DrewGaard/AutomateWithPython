import re
namesRegex = re.compile(r'Agent \w+')
secretString = 'Agent Molder gave the documents to Bob.'
print(namesRegex.findall(secretString))


print(namesRegex.sub('REDACTED', secretString))

newNamesRegex = re.compile(r'Agent (\w)\w*')
print(newNamesRegex.findall(secretString))

print(namesRegex.sub('REDACTED', secretString))
print(newNamesRegex.sub(r'Agent \1*****', secretString))

re.compile(r'''
\d\d\d    # area code
-         # first dash
\d\d\d    # first 3 digits
-         # second dash
\d\d\d\d  # last 4 digits''', re.VERBOSE)
