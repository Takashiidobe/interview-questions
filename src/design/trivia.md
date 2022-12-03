# Trivia Questions

1. [What is the difference between TCP and UDP?](./trivia/tcp-vs-udp.md)
2. What happens in between you pressing Enter in the address bar and the page loading?
3. What does a child process do when terminated?
4. How does caching work on your computer?
5. [How does a shell work?](./trivia/shell.md)
6. [How does `fork()` work?](./trivia/fork.md)
7. [How can you make memory allocation faster?](./trivia/faster-memory-allocation.md)
8. [How does virtual memory work?](./trivia/virtual-memory.md)
9. [How do you design an LRU cache to use less memory?](./trivia/lru.md)
10. [What is false sharing? What are its penalties?](./trivia/false-sharing.md)
11. [How can you make a system call faster?](./trivia/vdso.md)
12. How would you design a lock-free data structure in a language without a garbage collector? With a garbage collector? How would you implement a linked list, an array, and a hashmap lock-free?
13. What is branch prediction? What are some ways to speed up code that is inherently branchy?
14. What is NUMA? What does it do?
15. What does `constexpr` do in C++? Why is it useful?
16. What is the role of FPGA's in High Performance Computing?
17. [What does LTO do? Why is it important to use?](./trivia/lto.md)
18. [What does -ffast-math do? Why is it useful?](./trivia/ffast-math.md)
19. [What is SIMD?](./trivia/simd.md)
20. [How does a compiler compile your code? What is the difference between static and dynamic linking? How do symbols get resolved in each?](./trivia/compiling.md)
21. [What is the difference between multicast and TCP? How would you send packets from one client to subscribers?](./trivia/multicast.md)
22. (Incomplete) [How would you make a load balancer? How would you keep a server from being overloaded and fair?](./trivia/load-balancing.md)
23. [What is a named pipe? What is it used for?](./trivia/named-pipes.md)
24. [How does the Python GIL work?](./trivia/gil.md)
25. [How can you do asynchronous I/O in Linux?](./trivia/async-io.md)
26. [What is Kernel Bypass?](./trivia/kernel-bypass.md)
27. [What is a NIC?](./trivia/what-is-a-nic.md)
28. [What is the difference between read/recv and send/write](./trivia/read-vs-recv.md)
29. [What is the difference between a port and a socket?](./trivia/port-vs-socket.md)
30. [What is BGP? How does a packet get sent across the internet?](./trivia/bgp.md)
31. [What is the difference between a process and a thread?](./trivia/process-vs-thread.md)
32. [What is the linux directory hierarchy?](./trivia/linux-directories.md)
33. [How does a computer boot?](./trivia/booting.md)
34. [How would you debug X?](./trivia/debugging.md)
35. [What is EDNS Client Subnet](./trivia/edns.md)
36. [How does scheduling work in linux?](./trivia/scheduling.md)

Scheduling + Ray Tracing, + Data Structures

BFS/DFS

What is the minimum number of comparisons needed to find the second-largest element in a list.

OS related question: process vs thread, virtual memory - Algorithm question

How can you run multiple processes on one computer?

1) Given an array of list, determine if each number in the list can be written as a sum of 2 Fibonacci numbers. 2) Pandas questions. 3 & 4) Determine how many squares (q3) and rectangle (q4) can be formed given a bunch of points on the coordinate system.

Round 1)

- Given a string containing only the characters 'A' 'B' 'C' 'D', return the string when all adjacent "AB" / "BA" and "CD" / "DC" pairs have been removed.

- Given a graph (represented as an array) where nodes have value either 'A' or 'B', find the longest path where no two adjacent nodes have the same value.

Round 2)

- Physical memory vs virtual memory. You have 4GB physical, but you allocate an 8Gb buffer. Is this possible? If so, how? How is the memory actually read as we traverse the memory?

Linux overcommit would allow us to allocate as much memory as we want, and when we start using it, page faulting.

- Thread vs process, what's the difference? Talk about some common threading models.

- What are some methods of inter-process communication. Between threads. Between processes.

- Explain how a named pipe works (FIFO).

- What does the inline keyword do in C++? What are the pros and cons?

- How do virtual functions work in C++? Explain how vtable lookup works.

- Map vs unordered_map in C++, how is each one implemented under the hood. What data structure is used.
