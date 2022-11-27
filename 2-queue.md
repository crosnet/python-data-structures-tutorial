# Queue

When you want withdraw money at the ATM, you mostly meet a queue. The last person to join the queue is the last person to make a withdrawal. This is how queue works. Unlike stacks, queue uses the FIFO(First In, Last In) method to store items.

## Implementation

 Similar to stacks, a queue can be implemented using a list. However there are other methods for implementing queues in python.

- Using the list method: List methods such as `append()` and `pop()` can be used in implementing a queue in python. However using list requires more time resulting in O(n) time in performance rate. 
- Python also has the inbuilt `deque()` function which can be used instead of the list to obtain a best performance O(1). This function does not use the enqueue and deque methods. Rather, it uses the `append()` and `popleft()` methods. In order to implement this functioin in a queue in python, the deque function is first imported from python's collection library. for example:

```python
from collections import deque

#initializing a queue
my_queue = deque()
```
- Another method is the python inbuilt `Queue` module also used to implement queue.


## Common Queue Operations
- `Equeue()`: Inserts an item into the back of the queue in O(1) time
- `Dequeue()`: Removes an item from the front of the queue in O(n) time
- `isNull()`: Return true if the queue is zero in O(1) time
- `len()`: Returns the length of the queue in O(1) time.

## Example: Implement a Queue Using The Python built-in deque function.

```python
#import the deque module from the collectiion library
from collections import deque

#initialize the queue
our_queue = deque()

# now lets add some fruits into the queue
our_queue.append("apple")
our_queue.append("banana")
our_queue.append("orange")
our_queue.append("pawpaw")
our_queue.append("mango")

# lets see what we have so far in the queue
print("Our new queue")
print(our_queue)

# get the size of the queue
size = len(our_queue)
print(f"Size:", size)

# lets remove some of 2 fruits from the queue
our_queue.popleft()
our_queue.popleft()
print(our_queue)

# now lets get the new size
print(f"New size:", len(our_queue))

--------------------------------------------
Output:
Our new queue
deque(['apple', 'banana', 'orange', 'pawpaw', 'mango'])
Size: 5
deque(['orange', 'pawpaw', 'mango'])
New size: 3
```

## Problem To Solve: Implement a Queue using the Python Built-in Queue Module
This module is different from the one used in the example code above. Take note to not confuse the two. 
Your code should be able to do at least the following:

- Have a maxsize of 6
- Add at least 5 items in the queue after initializing and display the items.
- check if queue is full and display the size of the queue, should give true if full.
- Another item to the queue and check if it is full, should be true if full.
- Remove another item until queue is empty and check again.
- Display the size of the queue


Chech the [solution](2-solution.py) only after you have made an attempt to solve the problem on your own.

[Back to Welcome Page](welcome.md)
