arrayOfDessesrts = ["Cake", "Ice Cream", "Pudding", "Cream Caramel", "Basbousa"]

for i in range(len(arrayOfDessesrts)):
    print(i + 1, "-", arrayOfDessesrts[i])


for idx, dessert in enumerate(arrayOfDessesrts):
    print(idx + 1, "-", dessert)