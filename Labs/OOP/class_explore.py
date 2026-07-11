class A:
   def __init__(self, c):
       print("---------Inside class A----------")
       self.c = c
   print("Print inside A.")

   def alpha(self):
       c = self.c + 1
       return c

print(dir(A))
print("Instantiating A..")
a = A(1)
#print(a.alpha())

class B:
   def __init__(self, a):
       print("---------Inside class B----------")
       self.a = a

   print(a.alpha())
   d = 5
   print(d)
   print(a)

print("Instantiating B..")
b = B(a)
print(a)

'''
Step 1: Run the code and observe its output.
Take note of every line in the output and how it is different from the output you expected.

Step 2: Comment out lines #13, 14, 21, 24, 27 and 28. Run the code again. 

Step 3: Now remove the comment for lines 21 and 24. 
If you run the code at this point, it will throw an error, "NameError: name 'a' is not defined".
Take note of how you have passed the object a to the constructor of class B and the code still worked fine earlier.
Only when you tried to ‘use’ object a, did you get an error because it has not been instantiated. 
In other words, Python still does not know what ‘a’ means. 
The same will happen if you remove commenting next to line 28. 
To make the code work, now remove the # in front of line 14 and run it again.

Step 4: Remove the commenting for line 27 and 28.

Step 5: Finally remove all the remaining comments and run the code one more time. 
'''