import os

print(os.path.join('Documents', 'Automate Stuff with Python'))

os.getcwd()

print(os.path.getsize(os.getcwd()))

print(os.listdir(os.getcwd()))

totalSize = 0

for filename in os.listdir(os.getcwd()):
    if not os.path.join(os.path.join(os.getcwd(), filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join(os.path.join(os.getcwd(), filename)))

print(totalSize)
