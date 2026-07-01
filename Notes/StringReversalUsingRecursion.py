#Recursion
'''
Recursion in a nutshell is calling a method inside itself

It is helpful with logic that consists of repetitive steps that keep happening until a case is met
This case is what we call the [Base Case]

One example of recursion is reversing strings
'''

def ReverseString(str):
    #Base Case --> so that the recursion doesn't loop infinitely
    if len(str) == 0:
        return str
    #Recursive Case: calling the method again & again until you reach the base case above
    else:
        return ReverseString(str[1::]) + str[0]
    '''
    The Logic here is that you keep calling the method, changing the index position every time

    Let's say the string we're reversing is "Linux"
    this means that there will be 6 function calls
    
    Call 1 --> Keeps str[0] {L} at the end and calls the function again at index 1 {i}
    Call 2 --> Keeps str[0] {i} at the end and calls the function again at index 1 which is now {n}
    Call 3 --> Keeps str[0] {n} at the end and calls the function again at index 1 which is now {u}
    Call 4 --> Keeps str[0] {u} at the end and calls the function again at index 1 which is now {x}
    Call 5 --> Keeps str[0] {x} at the end and calls the function again at index 1 which is now {""}
    Call 6 --> str[0] is now "", which means len(str) is 0, which is our base case

    so it now goes up the call stack, because the first string was always kept at the end
    the string gets printed in reverse (x --> u --> n --> i --> L)
    '''

stringExample = 'Linux'
reversed = ReverseString(stringExample)
print(reversed)

# alternatively we can use the slice notation to reverse it
'''
The Slice notation in python goes [start:end:step]
notice how in the recursion method we relied on the slicing notation still by passing it as a
parameter to the recursive method

Alternatively, we can reverse it in a single line by leaving the start & end parameters empty
and instead having the step value be -1, which means we traverse from the end to the beginning
'''

anotherExample = "Ubuntu"
altReverse = anotherExample[::-1]
print(altReverse)