
# Basic data structures

I tried to focus more on Python and java for sections bellow.

* https://wiki.python.org/moin/TimeComplexity
* http://bigocheatsheet.com/

## Raw Arrays and Lists

Advantages:

* Fast RAMDOM access by index
* Keeps order
* allows duplicated elements

Disadvantages:

* Inserting or deleting on the middle is expensive, you have to move everything - O(n)
* When you have to append over initial allocation size, it's inefficient

## Linked lists

Advantages:

* Fast SEQUENTIAL access in one direction
* Keeps order
* Easy to insert in the middle

Disadvantages:

* Memory fragmentation
* random access element is O(n)

## Double linked lists

Same as single linked lists, but fast sequential access in both directions.

## Set

Advantages:

* Fast RANDOM access by both index and value - O(1)
* Good when you have to have unique elements
* Fast intersection and union operations - O(m+n)
* Fast difference operation - O(n)

Disadvantages:

* Can't hold duplicates
* Doesn't keep order of elements

## Dict (Hashmap)

Advantages and disadvantages are the same as sets, but you can associate key -> values

Hashmaps can be implemented with a list (array). It uses a hash function to hash an object to an index in the list.
As there might be collision, each item on the list should be a linked list of key value pairs.

A common hash function implementation is rest of division for list length:

```
hash = key.hashCode();
index = (hash & 0x7FFFFFFF) % tab.length;
```

Dict implementation in python - http://www.laurentluce.com/posts/python-dictionary-implementation/

## Stack

* FILO - First In Last Out
* Push and Pop operations
* It can be easily implemented with a single linked list - we keep a pointer to the root and every time push is performed,
a prepend to the root is performed. Every time pop is performed, we delete the root and the new root is the second element.

## Queue

* FIFO - First In First Out
* pushRight and popLeft operations
* It can be easily implemented with a single linked list, keeping a pointer to root and leaf. pushRight appends on the leaf,
popLeft deletes the root.

## HEAP, AVL and similar trees

### Binary tree definitions

Complete binary tree - balanced tree where all levels but the last are complete, at least.
Full binary tree - all levels should be complete, but tree might not be balanced.
Binary tree implementation usually considers all children to the left of the root are less and all children to the right are more than the root. Either that or the oposite.

Binary trees can be traversed:

* pre-order (root, then left, then right) - root first
* in-order (left, then root, then right) - sorted order
* post-order (left, then right, then root) - leaves first

### HEAP vs BST

Heap (priority queue) just guarantees that elements on higher levels are greater (for max-heap) or smaller (for min-heap) than elements on lower levels, whereas BST guarantees order (from "left" to "right"). If you want sorted elements, go with BST.

Heap is better at findMin/findMax (O(1)), while BST is good at all finds (O(logN)). Insert is O(logN) for both structures. If you only care about findMin/findMax (e.g. priority-related), go with heap. If you want everything sorted, go with BST.

In python, heaps are implemented by the heapq module - https://docs.python.org/2/library/heapq.html - by using arrays.

Heap is more limited than BST, but has faster insert operation average. BST has `findAny` operation, which heap doesn't.

                 BST       Heap
Insert average   log(n)    1
Insert worst     log(n)    log(n)
Find any worst   log(n)    n
Find max worst   1 (*)     1
Create worst     n log(n)  n

Details are here: https://stackoverflow.com/questions/6147242/heap-vs-binary-search-tree-bst/29548834#29548834

Summary is - there are 3 situations to decide:

* Sometimes you can sort upfront. In this case, you have a sorted array upfront and you don't need either heap or BST.
* Sometimes, you must check the min or max as you process elements. HEAP is suitable for this case.
* Sometimes, you must find any element on a collection as you insert elements. BST is useful in this case.

### AVL

AVL tree is a self-balancing binary search tree. When we refer to BST, we are usually referring to an AVL.

### Other trees

TODO complete this with red black and b-tree some day :D


