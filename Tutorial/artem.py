import artTest

# Run the tests
runTest = (9,)
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
def do_part_9():
    # Test method name resolving
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
    
    # Print the output
    myBc = MyBclass()
    print(myBc.do_math(2))
 
    # Test "multilevel" inheritance
    class MyL1Class:
        a = 1
        
        def print_name(self):
            print('Level ' + str(self.a) + ' class')
    
    class MyL2Class(MyL1Class):
        a = 2

        def output_funny_name(self, name):
            """Prints a funny name"""
            print('A funny name is ' + name)

    class MyL3Class(MyL2Class):
        a = 3

        def output_funny_name(self):
            """While using it, it overrides a method and hardcodes its output """
            super(MyL3Class, self).output_funny_name('Savr')

    myLClassTest = MyL3Class()
    # Call a method which is 3 levels "deep"
    myLClassTest.print_name()
    # Method name is found at level 3
    myLClassTest.output_funny_name()
    # Access a method of a parent's class
    super(type(myLClassTest), myLClassTest).output_funny_name('Gavr')

    # Test method overloading
    class PolymorphismTest:
        def test(self, *args):
            """Controler method"""
            if len(args) == 0:
                self.test_1()
            elif len(args) == 1:
                self.test_2(args[0])

        def test_1(self):
            """Overloaded method 1: 0 argument"""
            print('polymorth. method 1')

        def test_2(self, number):
            """Overloaded method 1: 1 argument"""
            print('polymorth. method ' + str(number))

    myPTest = PolymorphismTest()
    # print(dir(myPTest))

    myPTest.test()
    myPTest.test(2)

     # Test method overloading
    class BaseToChildTest:
        def mym1(self):
            print("mym1")

    class BaseToChildTest2(BaseToChildTest):
        def mym2(self):
            print("mym2")

    class BaseToChildTest3(BaseToChildTest):
        def mym3(self):
            print("mym3")

    myObjTest = BaseToChildTest()

    print("enter 1-BaseToChildTest")
    print("enter 2-BaseToChildTest2")
    print("enter 3-BaseToChildTest3")
    usrInput = int(input())

    if (usrInput == 1):
        myObjTest.mym1()
    elif(usrInput == 2):
        myObjTest.mym2()
    elif(usrInput == 3):
        myObjTest.mym3()


partsDict.update({9: do_part_9})

# Iterate
for i in runTest:
    if i in partsDict:
        # Part title
        artTest.start_of_part_print(i)
        
        # Call the corresponding function
        partsDict[i]()
        
        # End of the part
        artTest.end_of_part_print(i)
