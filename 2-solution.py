"""
CSE 212
BYU-Idaho
Author: Emmanuel Odonkor
queue-tutorial  Problem - solution
"""

from queue import Queue
# initialise a queue with the required size
our_queue = Queue(maxsize = 6)

#add items to the queue
our_queue.put("apple")
our_queue.put("banana")
our_queue.put("mango")
our_queue.put("pawpaw")
our_queue.put("orange")

#check if the queue is full, should print true if full.
print(f"Queue isFull: ",our_queue.full())
#display the current size of the queue
print(f"The queue size after adding items is", our_queue.qsize())
#add another another to the queue
our_queue.put("melon")
#check again if queue is empty
print("After adding another item")
print(f"Queue isFull:",our_queue.full())

# now remove items until the queue is empty
print("RemOving items...")
print("ITEMS REMOVED:")
print(our_queue.get())
print(our_queue.get())
print(our_queue.get())
print(our_queue.get())
print(our_queue.get())
print(our_queue.get())

#get the size of the queue
print("Getting the size of the queue...")
print(f"The size of the queue is now:", our_queue.qsize())