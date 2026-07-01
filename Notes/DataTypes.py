# Use type(variable) to figure out or double check a type.

'''
#Dictionary 
#Basically an object 
#### Very important for Web APIs, since you get & post data in objects.

value1 = 22
value2 = 44
dictionaryExample = {'val1': value1, 'val2':value2}

print(dictionaryExample['val2'])
'''

'''
#SEQUENCE TYPES
#1. Strings "" --> name = "Hazem", each letter / character in this string has an index. ('H' being name[0])
    # a string is technically a sequence of letters.

    # name = 'Hazem'
    # print(name[2]); #Outputs 'z'
    # print(len(name)) #Outputs 5

#2. Lists [] --> Basically an array
    #cars = ["Honda", "Toyota", "Ford", "BMW"]
            #   0        1         2      3

#3. Tuples () --> an array that's immutable, which means can't be modified 
    #tuples can be good for storing different modes

    #modes = ('admin', 'resturant', 'deliveryPerson', 'customer')

#4. Sets {} --> An array of unique items, written in curly braces

    items = {1, "A lot", 5, True}
    type(items) #Outputs <class 'set'>    
'''