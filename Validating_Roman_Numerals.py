# You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.

# Input Format

# A single line of input containing a string of Roman characters.

# Output Format

# Output a single line containing True or False according to the instructions above.

# Constraints

# The number will be between
# and

# (both included).

# Sample Input

# CDXXI

# Sample Output

# True


regex_pattern = r"^M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$"	

