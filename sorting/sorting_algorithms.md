# Sorting algorithms

## Bubble sort

"Brute force" - O(n^2)

```
For every item of the list,
    compare to every item of the list,
        and swap everytime you find smaller item
```

```python
def bubble(seq):
    length = len(seq) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(length):
            if seq[i] > seq[i+1]:
                sorted = False
                seq[i], seq[i+1] = seq[i+1], seq[i]
```
## Selection sort

"Better Brute force" - O(n^2)

```
For every item of the list,
    compare to every non-sorted item of the list to find minimum,
    Swap item with minimum found and count it as sorted
```

```python
def selection_sort(seq):
    """Sort the mutable sequence seq in place and return it."""
    for i in reversed(range(len(seq))):
        greatest = max(range(i + 1), key=seq.__getitem__)
        seq[i], seq[greatest] = seq[greatest], seq[i]
    return seq
```

## Merge sort 

First divide to conquer. Split the list in 2 halves and sort each half.
Then combine both sorted halves by taking smaller element of each list first.

```python
def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)
````

## Quick sort 

Quick sort works by first selecting a pivot element from the list. It then creates two lists, one containing elements less than the pivot and the other containing elements higher than the pivot. It then sorts the two lists and join them with the pivot in between. Just like the Merge sort, when the lists are subdivided to lists of size 1, they are considered as already sorted.

```python
def quick_sort(items):
    """ Implementation of quick sort """
    if len(items) > 1:
        pivot_index = len(items) / 2
        smaller_items = []
        larger_items = []

        for i, val in enumerate(items):
            if i != pivot_index:
                if val < items[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)

        quick_sort(smaller_items)
        quick_sort(larger_items)
        items[:] = smaller_items + [items[pivot_index]] + larger_items
```

### Merge sort vs Quick sort

* Quick sort is an IN-PLACE Algorithm while Merge sort is not -> It means that Quick sort does not require any additional memory while executing, the argument is modified

* Quick Sort is NOT a stable sorting algorithm while Merge is -> A Sorting algorithm is called stable if it preserves the order of occurance of elements in the unsorted array.

https://www.quora.com/What-is-the-difference-between-quicksort-and-mergesort

