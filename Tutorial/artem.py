import artTest

# Run the tests
runTest = (9,)


# Part 1, 3
partNum = 1
if 1 in runTest:
    artTest.start_of_part_print(partNum)
    
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

    artTest.end_of_part_print(partNum)


# Part 4
partNum = 4
if partNum in runTest:
    artTest.start_of_part_print(partNum)
    
    # Does the in keyword work with numbers, instead of vars
    if 1 in [1,2,3]:
        print("1 is in 1,2,3")

    # Testing Documentation Strings
    def doc_str_test():
        """This function serves the test of doc strings."""
        pass

    # Printing a docstring
    print(doc_str_test.__doc__)

    artTest.end_of_part_print(partNum)


# Part 5
# no code, sorry
partNum = 5
if partNum in runTest:
    pass


# Part 6
partNum = 6
if partNum in runTest:
    artTest.start_of_part_print(partNum)
    
    # Add a module
    # In the beggining of the module

    # Rename an imported module's function
    tpt = artTest.two_plus_two
    tpt()

    # List names of the imported module
    print(dir(artTest))
    
    
    artTest.end_of_part_print(partNum)


# Part 7
# Testing string formatting
partNum = 7
if partNum in runTest:
    artTest.start_of_part_print(partNum)
    
    # Import sys objects
    import sys
    
    print('{} equals 2'.format(2))
    
    # Receive input using stdin
    pr = sys.stdin.readline()
    print(f'user input = {pr}')
    
    # Receive input using input()
    prp = input('Enter your input, sir: ')
    print(f'user input = {prp}')
    

    artTest.end_of_part_print(partNum)


# Part 9
# Base class
partNum = 9
if partNum in runTest:
    artTest.start_of_part_print(partNum)
    
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

    artTest.end_of_part_print(partNum)
