# Prompt Engineering Logs

## Person 1: Core Logic Edge Cases
**Prompt used:** 
"I wrote a Python function that calculates a match score by comparing a student's skills (list of strings) to an internship's required skills (list of strings). What edge cases and invalid inputs should I validate against?"

**AI Response Summary:**
The AI suggested validating against:
1. Incorrect data types (passing strings or integers instead of lists).
2. Empty lists (student has no skills, or internship requires no skills).
3. Case sensitivity and whitespace (e.g., "Python" vs " python ").
4. Missing dictionary keys when processing the broader database.

**How I applied this:** 
I added `TypeError` checks for list validation, implemented a division-by-zero safeguard for empty internship skills, and used `.strip().lower()` to handle case and whitespace discrepancies.
