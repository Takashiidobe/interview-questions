# Design a Text Editor

First steps involve fast editing of a file.

- Consider a RAM limited machine, where files are consistently larger than memory. What should we do?
- How do we support fast updates/deletes to any location in the file?
- What representation of the file in-memory works to replicate the disk representation?

## Extras

- How would you support undo/redo? Extra buffers for copy/pasting?
- What happens if the file has the same string over and over again in the file? Can we use memory better by interning certain parts of the text file?
- How do we make the file crash tolerant? What happens if the app crashes, is killed, or there's a hard drive failure? We should never lose data. How do we fulfill that?
