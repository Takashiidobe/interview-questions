# How do caches work on your computer?

on x86, cache lines are 64-bytes, and look like the following:

| Type | Size | Latency     |
|------|------|-------------|
| L1   | 64KB | 1 cycle     |
| L2   | 9MB  | 10 cycles   |
| L3   | 12MB | 50 cycles   |
| RAM  | 32GB | 200 cycles  |
| SSD  | 2TB  | 3000 cycles |
| HDD  | 16TB | 1.5M cycles |

There are also caches for the Translation Lookaside Buffer (TLB) which are 1024 pages.

Caching is used to make memory accesses faster: in the table above, you can see that smaller caches are much faster, but slower memory can store more memory.

Caches are associative (shared between cores), so they might not be as large per core as you might expect (this computer have 1MB+ of cache, but 12 cores can access it, so they all have to share it).
