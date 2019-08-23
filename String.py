## lets start with the python string

x = 'My string'
print(x)

print('Hello' + ' ' + 'World')

print('Hello{}'.format('World'))

print('{} {}'.format('Hello', 'WOrls'))

print('{1}{0}'.format('Hello', 'World'))

print('{h}{w}'.format(h='Hello', w='world'))

# =    Assignment

# Arithmetic Operators
# --------------------
# +    Addition
# -    Subtraction
# *    Multiplication
# /    Division
# //   Floor Division
# %    Modulo
# **   Power

x, y = 20,30;
print(x+y)

print(x/y)
print(x//y)



# Comparison Operators
# --------------------
# ==   Equal To
# >    Greater Than
# >=   Greater Than or Equal To
# <    Less Than
# <=   Less Than or Equal To
# !=   Not Equal

if x==y:
	print('its equal')

if(x != y):
	print('not equal')

if(x > y or x < y):
	print(x,y)

if(20>= x <= 30):
	print(x)

# Boolean Operators
# -----------------
# and
# or
# not
# */

if(x < y or x == y):
	print(x,'is greater')

if(x < y and x == y):
	print(x, 'is less')