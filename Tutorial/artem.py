import artTest

# Run the tests
runTest = (1,4,5,6,7,9)
partsDict = {}

# Part 1, 3
def do_part_1():
    # 2+2
    print(2+2)

    name = 'Savr'
    # Does not work b/c all strings are interpreted as strings (not chars)
    # name[0] = 's'

    # does not work without the "+" operand
    print('hello, ' + name)

    # Out of range error
    # print(name[5])
    # name [5] = 'i'

    # Avoid the out of range error
    print('range test: ' + name[5:])

    # Display the length of a string
    print(len(name))

    letters = [ 't', 'e', 's', 't' ]
    letters[0] = 'bab'

    print(letters)

    # Emptry string is false
    while '':
        print("while true")

partsDict.update({1: do_part_1})

# Part 4
def do_part_4():
    # Does the in keyword work with numbers, instead of vars
    if 1 in [1,2,3]:
        print("1 is in 1,2,3")

    # Testing Documentation Strings
    def doc_str_test():
        """This function serves the test of doc strings."""
        pass

    # Printing a docstring
    print(doc_str_test.__doc__)

partsDict.update({4: do_part_4})

# Part 5
# no code, sorry
def do_part_5():
    pass

partsDict.update({5: do_part_5})


# Part 6
def do_part_6():
    # Add a module
    # In the beggining of the module

    # Rename an imported module's function
    tpt = artTest.two_plus_two
    tpt()

    # List names of the imported module
    print(dir(artTest))

partsDict.update({6: do_part_6})


# Part 7
# Testing string formatting
def do_part_7():
    # Import sys objects
    import sys
    
    print('{} equals 2'.format(2))
    
    # Receive input using stdin
    print("Enter stuff: ")
    pr = sys.stdin.readline()
    print(f'user input = {pr}')
    
    # Receive input using input()
    prp = input('Enter your input, sir: ')
    print(f'user input = {prp}')

partsDict.update({7: do_part_7})


# Part 9
# Base class
def do_part_9():
    class MyBclass:
        """My base class containing the "main" do_math() func"""
        def do_math(self, num):
            # Create a new instance of the derived class
            myDc = MyDclass()
            
            # Call the overriden func within the "main" func
            return num + myDc.do_math()

    class MyDclass(MyBclass):
        """My derived class that overrides the do_math() func"""
        def do_math(self):
            return 2

    # Test the output
    myBc = MyBclass()
    print(myBc.do_math(2))

partsDict.update({9: do_part_9})

# Iterate
for i in runTest:
    if i in partsDict:
        artTest.start_of_part_print(i)
        
        partsDict[i]()
        
        artTest.end_of_part_print(i)
