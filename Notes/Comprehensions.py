#Comprehensions provide a short-hand and elegant way of updating sequences.

'''
#1 - LIST COMPREHENSION []
[<expression> for x in <sequence> if <condition>]

'''
data = [2,3,5,7,11,13,17,19,23,29,31]

# Ex1: List comprehension: updating the same list
data = [x+3 for x in data]
print("Updating the list: ", data)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x*2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x%4 == 0 ]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x%4 == 0 ]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x%9 == 0]
print("Nines: ", nines)

'''
#2 - DICTIONARY COMPREHENSION {}
{key: value for (key, value) in <sequence> | (sequence1, sequence2) if <condition>}

'''

# Using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

# Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)

'''
#3 - SET COMPREHENSION {}
{<expression> for x in <sequence> if <condition>}
like lists, but with curly braces to terminate duplicates
'''

set_a = {x for x in range(10, 20) if x not in [12, 14, 16]}
print(set_a)

'''
#4 - GENERATOR COMPREHENSION ()
(<expression> for x in <sequence> if <condition>)
Generator comprehensions are also very similar to lists with the variation of using curved brackets instead of square brackets. 
They are also more memory efficient as compared to list comprehensions.
'''
data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for x in gen_obj:
    print(x, end= " ") #end = " ", prints the values next to each other instead of the default \n new line

'''
WHY COMPREHENSIONS?
    The map function & list comprehensions effectively do the same job of modifying iterator sequences like the ones in examples above
    They aren't necessarily more efficient, but they offer great readability & ease of use
    They also return the lists directly unlike the map function which returns a map object

    Bottom line is, opt for the use of map & filter functions as they are the better choice for bigger lists, but comprehensions are good to know
'''