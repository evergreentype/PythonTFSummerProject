import artTest

# Run the tests
runTest = (1, 4, 5, 6, 7,)


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

    artTest.end_of_part_print()


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

    artTest.end_of_part_print()


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

    artTest.end_of_part_print()


# Part 7
# Testing string formatting
partNum = 7
if partNum in runTest:
    artTest.start_of_part_print(partNum)
    
    print('{} equals 2'.format(2))

    artTest.end_of_part_print()
