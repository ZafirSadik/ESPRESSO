# ESPRESSO

This code implements ESPRESSO algorithm for two level logic minimization using python.

The full ESPRESSO algorithm is complex and envolves multiple sophisticated steps like expansion, reduction and irredundent cover extraction. It also handles don't care conditions.

This code is a simplified version of the full ESPRESSO algorithm. This process focuses on combining terms that differ only one variable which is suitable for small-scale logic functions. We tested it for up to 10 variables and the code works fine.

Implementation Challanges & Solutions:
1. Combining Terms Correctly: The first challange was accurately combining terms that differ by only one variable along with successfully handling don't care conditions.
   Solution: The **combine_terms** function was used to check pairs of terms. 
