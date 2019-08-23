print("This is the lecture on string fundamentals and some advanced concept")
### Here we gonna discussed something about the string 

#-------------- Definition---------------

#String is nothing but the collection of characters. Its one of the widely used object in Python and stores any text 

#------------ String declaration and definition -----------
my_string_one = "This is my string"
my_string_two =  "This is my another string"

#--------- String Concatenation ---------------
print(my_string_one + my_string_two)   #This is my stringThis is my another string
print(my_string_one+ ' ' + my_string_two)  # This is my string This is my another string
#print(my_string_one +  1)   # this will error - TypeError: must be str, not int

#--------- Type casting other datatypes to str -------------
print(my_string_one + ' ' +  str(1) )

#-------------- Formatting --------------
print('{} {}'.format(my_string_one, 1))   # always make sure those placeholders{} neddes to be in quotes
print('{0} {1}'.format(my_string_one, 1))
print('{string_one} {number}'.format(number=1, string_one=my_string_one))
#NOTE: We can also use double quotes in place of single quotes

#----------F - String -----------------
# there is another way of concatenating string with any other datatype and ie. f-string and this is introduced in <= 3.6 versions
print(f'{my_string_one} 1234')
print(f'{my_string_one} True')

#--------- String methods-------------
# since string is an object there properties and methods associated with the same. Lets discuss some of them

print(len(my_string_one))  # this will return the length of string including blank spaces between words

print(my_string_one.capitalize())  # This will capitalize the first letter of the first word in the string - This is my string

print(my_string_one.isalpha())

my_string_three = '{} {}'.format(my_string_one, 123)  

print(my_string_three.isalnum())  # return true if there is numbers and characters both

print(my_string_one.split())    # split the string and return the list of words within that string - ['This', 'is', 'my', 'string']

print(my_string_one.upper()) # this will convert all the string characters into uppercase - THIS IS MY STRING

print(my_string_one.lower())  # this will convert the string into lowercase - this is my string

print(my_string_one.title())   # this will capitalize every first letters of words within string -This Is My String

print(my_string_one.replace('This', 'It\'s'))   # this will replace 'This' with 'It's'- It's is my string

print(my_string_one.rfind('Th', 0 , -1))

print(my_string_one.rsplit(sep='t'))   # in rsplit we can specify from where we can split - ['This is my s', 'ring']