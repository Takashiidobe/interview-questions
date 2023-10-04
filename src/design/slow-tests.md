# Slow Tests

You're a DevOps engineer at BigCo. Your test suite for a service has hundreds of thousands of tests, and they take hours to run. You've bought the best computer that money can buy to run them, so we can't buy a better computer.

How do you make them run faster?


## Solutions

The solution is to parallelize tests. But sometimes tests have a dependency, where they only pass if some previous test runs.

For example:

A -> B: A + B pass
B -> A: B fails, A passes

Thus, you must run A -> B. How do you prevent these problems from happening in the future?

How do you also deal with this while maintaining parallelism?
