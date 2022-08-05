Design a data structure that supports two operations:

`add()` which takes an x and y coordinate:

And `minRectangle()`, which returns the area of the minimum rectangle
that covers all the coordinates currently in the data structure.

For example:

`add(1, 1)`
`minRectangle()` returns 1

`add(4, 4)`
`minRectangle()` returns 9

## Solution

Use two self-balancing trees to keep track of the x and y coordinates.
Have one data structure keep track of the xs, and one data structure
keep track of the ys.

You can calculate the minimum x, maximum x, minimum y, and maximum y
from the data structures.

Or you could use a heap, since we have a guarantee that we'll never need
to delete.

## Follow Up

What happens if you need to be able to delete?

If so, a heap no longer provides the correct answer -- unless you're
fine with O(n) time for a deletion.
