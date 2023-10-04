# Design a web crawler

- A web crawler reads web pages and then summarizes their content.

Concerns:

- How do we guarantee fast performance? The web is large.
- How do you handle incorrect/adversarial HTML?
- How do we prevent loops? If one site references another site, it references another site, and that site references the first site.
- How do you rank pages? Closeness + relevancy to search queries is important.

Extras:

- Assume that you have a vocabulary of 2000 english words. How do you search for queries like "System design" OR "leetcode" or "System Design" AND "leetcode"?
- How do you handle closeness of those queries as well?
- How would you store the results of your web crawler on disk?
