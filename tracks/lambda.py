# test lamba function
# No imports needed for this one

even = lambda num: num%2 == 0

# number = raw_input('What is the number you want to check? ')
# number = str(number)
# even(number)


reverse = lambda s: s[::-1]

phrase = raw_input('What is the string you want to reverse? ')
print reverse(phrase)
