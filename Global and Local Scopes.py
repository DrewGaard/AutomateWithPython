eggs = 42 # global variable

def spam():
    eggs = 42 # local variable
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
    print(eggs)

print('Some code here.')
print('Some more code.')
spam()
bacon()
print(eggs)
