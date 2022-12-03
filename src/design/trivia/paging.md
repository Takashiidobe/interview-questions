# Paging

Paging divides the linear address space into fixed-sized pages. The most common size is 4KB, but 2MB and 1GB are also common on x86_64 on linux.

The MMU does translation of a page location to the linear address space.

The Linux kernel uses 4-level page tables:

- Page Global Directory
- Page Upper Directory
- Page Middle Directory
- Page Table Entry

The kernel is allowed to use the top 16-bits, and userspace gets 48-bits.
