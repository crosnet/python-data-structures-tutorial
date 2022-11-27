"""
CSE 212
BYU-Idaho
Author: Emmanuel Odonkor
set-tutorial  Problem - solution
"""

def modify_set(values):
    #initialize the set
    my_set = set()
    #loop through all the values in the list
    for n in values:
        # check for the even numbers
        if n % 2 == 0:
            #add the even numbers to the new set
            my_set.add(n)
    print(my_set)

modify_set([0, 1, 2, 3, 4, 6, 10, 15, 16])
