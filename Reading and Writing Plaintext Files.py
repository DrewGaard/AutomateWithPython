import os, shelve

helloFile = open(os.path.join(os.getcwd(), 'hello.txt'), 'r')

baconFile = open('bacon.txt', 'w')

content = helloFile.read()

print(content)

baconFile.write('HELLO THERE!!!!\n')

baconFile.write('CLICK HERE FOR FREE BACON!!!!\n')

baconFile.close()

print(content)

shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])

shelfFile.close()

helloFile.close()
