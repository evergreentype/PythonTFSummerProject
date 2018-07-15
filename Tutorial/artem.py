# Part 1, 3
def part1_2_3_tests():
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
    print(name[5:])

    # Display the length of a string
    print(len(name))

    letters = [ 't', 'e', 's', 't' ]
    letters[0] = 'bab'

    print(letters)

    # Emptry string is false
    while '':
        print("while true")


# Part 4
def part4_tests():
    # Does the in keyword work with numbers, instead of vars
    if 1 in [1,2,3]:
        print("1 is in 1,2,3")

    # Testing Documentation Strings
    def doc_str_test():
        """This function serves the test of doc strings."""
        pass

    # Printing a docstring
    print(doc_str_test.__doc__)


# Part 5
# no code, sorry
def part5_tests():
    pass

# Part 6
def part6_tests():
    # Add a module
    import sys, artTest

    # Rename an imported module's function
    tpt = artTest.two_plus_two
    tpt()

    # List names of the imported module
    print(dir(artTest))


# Part 7
# Testing string formatting
def part7_tests():
    partNum = 7
    print(f'Part {partNum}')
    
    print('{} equals 2'.format(2))


# Run the tests
# part1_2_3_tests()
# part4_tests()
# part5_tests()
# part6_tests()
part7_tests()
