# ESPRESSO

This code implements the ESPRESSO algorithm for two-level logic minimization using python.

The full ESPRESSO algorithm is complex and involves multiple sophisticated steps like expansion, reduction and irredundant cover extraction. It also handles don't care conditions.

This code is a simplified version of the full ESPRESSO algorithm. This process focuses on combining terms that differ only one variable which is suitable for small-scale logic functions. We tested it for up to 10 variables and the code works fine.

<br><br>
**Implementation Overview:**
   1. Reading and Parsing the PLA file: The code reads the input PLA file and separates it into header directives and logic terms.
   2. Parsing the Logic Terms: The raw logic terms are converted into a structured format for processing.
   3. Minimizing the Logic Terms: The logic expressions ate simplified by combining terms that differ by only one variable.
   4. Combining Terms: Two terms that differ by only one variable position are combined and the new combined terms are added.
   5. Removing Redundant Terms: Duplicate terms are eliminated from the minimized term list.
   6. Writing the Minimized PLA File: The minimized terms are formatted to write the output file. Then an output PLA file is created, preserving the original format.
   7. Main execution Flow: The function **main()** coordinates the overall execution of the program.

<br><br>
**Code Execution:**

Write an input file named "input.pla" and keep it in the same directory as the code. Run the code. An output file named "output.pla" will be generated with the minimized logic output.
