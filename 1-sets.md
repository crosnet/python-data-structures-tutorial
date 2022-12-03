# Sets
In math or algebra, we have sets. Sets in math is used to different store values to perform calculations. The same applies to programming. In programming, there are four built-in data structure for collecting and storing data in a variable. 
- List
- Dictionary
- Tuple
- Set

A set is a data structure that collects and stores data in a variable, It has unique features different from the other types. A set can be created by placing all the items into the curly brackets seperated by a comma. A `set()` constructor can also be used to create a set and append values into it. Below is an example of a python set from *pynative.com*.

![python set](python-sets.jpg)

- A set can contain different data types(boolean, strings, integers)
- A set does not contain duplicate values: This feature allows us to create a set from a list without having to worry about duplicate values.  
- It's values can be unordered: Which means you cannot tell in which order the items would be.
- And they are unchangeable: Because the values are unchangeable does not mean items cannot be removed or added.
- A set can be used to find values in a list or add and remove values in 0(1) time.
- A set can be used to perform mathematical operations like finding the union and intersection of two or more sets.

```python
    #testing for unordered characteristic
    se1 = {1,2,3,4,0,1,2}
    #testing for different data types
    set2 = {"kate", 10, 5.1}
    print(set1)
    print(set2)
-------------------------
output
set1 = {0,1,2,3,4}
set2 = {5.1, 10, "kate"}
```


# Example: Modifying A Set
```python
def modify_set(values):
    my_set = set()
    for n in values:
        my_set.add(n)
    print(my_set)

    # add another fruit to the set and display
    my_set.add("kiwi")
    print(my_set)
    # remove kiwi from the set
    my_set.remove("kiwi")
    # get the length of the set and display
    length = len(my_set)
    print(f"Length:",length)

modify_set(["apple", 1, "mango", 2, "orange"])
------------------------------------------
Output:
# Created the set from the list
{1, 2, 'mango', 'orange', 'apple'}
#added kiwi to the set
{1, 2, 'mango', 'kiwi', 'orange', 'apple'}
#got the length of the set
Length: 5

```

# Problem to Solve: Find A Unique Value From A List.

Write a python program to find all the even numbers in a list of integers and create a set with the found values. 

Check the [solution](1-solution.py) only after you have made an attempt to solve the problem on your own.

[Back to Welcome Page](welcome.md)
