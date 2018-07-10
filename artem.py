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

# Emptry stirng is false
while '':
    print("while true")
