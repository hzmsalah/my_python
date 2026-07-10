# Define class MyFirstClass
class MyFirstClass:
    # Define string variable called index
    index = "Author-Book-Year"

    def __init__(self):
        print("Who wrote this?")
    
    # Define function hand_list()
    def hand_list(self, philosopher, book, year):
        print(MyFirstClass.index)
        # variable + “ wrote the book: ” + variable
        print(philosopher,"Wrote the book",book,"in the year",str(year))

# Call function handlist()
whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu","The Art Of War",500)
