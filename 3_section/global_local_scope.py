test = 42 # global scope

def func():
    test = 42 # local variable

def spam():
    print(eggs)

eggs = 42
# spam()

# specifically telling python to edit the global variable
def sandwich():
    global eggs
    eggs = 15
    print(eggs)

eggs = 42
sandwich()
print(eggs)
