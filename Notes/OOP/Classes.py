'''Creating Classes in Python'''

#1 Define The Class
'''Classes are the blueprint for the objects you later instantiate
    They comprise of attributes (Variables) & behaviors (Methods)
'''
class Pet:
    
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
    '''This is called a constructor
    It allows us to initialize unique instance attributes
    '''

    def speak(self):
        if self.kind == "Dog":
            return f"{self.name} says woof :D"
        elif self.kind == "Cat":
            return f"{self.name} says Maow -_-"
        

#2 Declare an instance of the Class
'''Essentially creating an object by assigning it to a variable'''

bolt = Pet("Bolt", "Dog")
shawqy = Pet("Shawqy", "Cat")

#3 Accessing attributes or methods
print(bolt.speak())
print(shawqy.speak())
print(Pet("Rex","Dog").speak())
