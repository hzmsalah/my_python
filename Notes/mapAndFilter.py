'''
The Map & Filter functions are built-in functions
that enables efficient data transformation and processing by 
applying operations to entire iterables (like lists or tuples) 
without using explicit loops.

It's why you can use comprehensions as an alternative because they pretty much do the same thing
'''


'''
# map(function, iterable)
returns a map object
the function here should be the data transformation you'd like to make
and the iterable is the data structure you'd like to traverse

'''

list_of_numbers = [2,4,6,8,10]

def doubling(number):
    return number*2

doubled_list = map(doubling, list_of_numbers)
print(doubled_list) #prints <map object at 0x00000..>
for number in doubled_list:
    print(number)

'''
# filter(function, iterable)
returns a filter object
the function here should be the one filtering
and the iterable is the data structure you'd like to traverse
'''

list_of_names = ['amir','farid','salma','reda','mariam','ahmed','amal','gamal','sarah']

def letter_a_names(string):
    if string[0] == "a":
        return string
    
names_containing_a = filter(letter_a_names, list_of_names)
print(names_containing_a) #prints <filter object at 0x00000...>
for name in names_containing_a:
    print(name)
