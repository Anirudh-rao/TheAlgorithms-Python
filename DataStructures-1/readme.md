# Datastructures-1

## Stack
A stack is a linear data structure that follows the principle of `Last In First Out (LIFO)`. This means the last element inserted inside the stack is removed first.
You can think of the stack data structure as the pile of plates on top of another.

### Basic Operations of Stack
There are some basic operations that allow us to perform different actions on a stack.

1. Push: Add an element to the top of a stack
2. Pop: Remove an element from the top of a stack
3. IsEmpty: Check if the stack is empty
4. IsFull: Check if the stack is full
5. Peek: Get the value of the top element without removing it

### Working of Stack Data Structure
The operations work as follows:

1. A pointer called TOP is used to keep track of the top element in the stack.
2. When initializing the stack, we set its value to -1 so that we can check if the stack is empty by comparing TOP == -1.
3. On pushing an element, we increase the value of TOP and place the new element in the position pointed to by TOP.
4. On popping an element, we return the element pointed to by TOP and reduce its value.
5. Before pushing, we check if the stack is already full
6. Before popping, we check if the stack is already empty

### Stack Time Complexity
1. For the array-based implementation of a stack, the push and pop operations take constant time, i.e. O(1).

### Applications of Stack Data Structure
Although stack is a simple data structure to implement, it is very powerful. The most common uses of a stack are:

1. To reverse a word - Put all the letters in a stack and pop them out. Because of the LIFO order of stack, you will get the letters in reverse order.
2. In compilers - Compilers use the stack to calculate the value of expressions like 2 + 4 / 5 * (7 - 9) by converting the expression to prefix or postfix form.
3. In browsers - The back button in a browser saves all the URLs you have visited previously in a stack. Each time you visit a new page, it is added on top of the stack. When you press the back button, the current URL is removed from the stack, and the previous URL is accessed.


## Queue Data Structures

A queue is a useful data structure in programming. It is similar to the ticket queue outside a cinema hall, where the first person entering the queue is the first person who gets the ticket.
Queue follows the First In First Out (FIFO) rule - the item that goes in first is the item that comes out first.

### Basic Operations of Queue
A queue is an object (an abstract data structure - ADT) that allows the following operations:

1. Enqueue: Add an element to the end of the queue
2. Dequeue: Remove an element from the front of the queue
3. IsEmpty: Check if the queue is empty
4. IsFull: Check if the queue is full
5. Peek: Get the value of the front of the queue without removing it

### Working of Queue
Queue operations work as follows:

1. two pointers FRONT and REAR
2. FRONT track the first element of the queue
3. REAR track the last element of the queue
4. initially, set value of FRONT and REAR to -1

### Enqueue Operation
1. check if the queue is full
2. for the first element, set the value of FRONT to 0
3. increase the REAR index by 1
4. add the new element in the position pointed to by REAR

### Dequeue Operation
1. check if the queue is empty
2. return the value pointed by FRONT
3. increase the FRONT index by 1
4. for the last element, reset the values of FRONT and REAR to -1


### Complexity Analysis
The complexity of enqueue and dequeue operations in a queue using an array is O(1). If you use pop(N) in python code, then the complexity might be O(n) depending on the position of the item to be popped.

### Applications of Queue
1. CPU scheduling, Disk Scheduling
2. When data is transferred asynchronously between two processes.The queue is used for synchronization. For example: IO Buffers, pipes, file IO, etc
3. Handling of interrupts in real-time systems.
4. Call Center phone systems use Queues to hold people calling them in order.


### Types of Queue

### 1. Circular Queue:
A circular queue is the extended version of a regular queue where the last element is connected to the first element. Thus forming a circle-like structure.

### How Circular Queue Works
Circular Queue works by the process of circular increment i.e. when we try to increment the pointer and we reach the end of the queue, we start from the beginning of the queue.

Here, the circular increment is performed by modulo division with the queue size. That is,

```
if REAR + 1 == 5 (overflow!), REAR = (REAR + 1)%5 = 0 (start of queue)

```
#### Circular Queue Operations
The circular queue work as follows:

1. two pointers FRONT and REAR
2. `FRONT` track the first element of the queue
3. `REAR` track the last elements of the queue

initially, set value of FRONT and REAR to -1

#### 1. Enqueue Operation:

1. check if the queue is full
2. for the first element, set value of FRONT to 0
3. circularly increase the REAR index by 1 (i.e. if the rear reaches the end, next it would be at the start of the queue)
4. add the new element in the position pointed to by REAR

#### 2. Dequeue Operation:

1. check if the queue is empty
2. return the value pointed by FRONT
3. circularly increase the FRONT index by 1
4. for the last element, reset the values of FRONT and REAR to -1

However, the check for full queue has a new additional case:
```
Case 1: FRONT = 0 && REAR == SIZE - 1
Case 2: FRONT = REAR + 1

```
The second case happens when REAR starts from 0 due to circular increment and when its value is just 1 less than FRONT, the queue is full.




