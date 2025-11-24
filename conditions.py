# ---------------------------------------------------------
# Python Conditions - Full Examples with English Explanations
# ---------------------------------------------------------

name = "ron"

# ---------------------------------------------------------
# 1. IF STATEMENT
# The 'if' block runs only if the condition is True.
# ---------------------------------------------------------

if name == "maor":
    print("condition is true!")
print("this line runs anyway!")

# ---------------------------------------------------------
# 2. IF–ELSE STATEMENT
# If the condition is True → run the 'if' block
# Else → run the 'else' block
# ---------------------------------------------------------

if name == "maor":
    print("condition is true!")
else:
    print("condition is false!")
print("this line runs anyway!")

# ---------------------------------------------------------
# 3. IF – ELIF – ELSE STATEMENT
# Multiple conditions are checked in order.
# Python stops at the first condition that is True.
# ---------------------------------------------------------

if name == "maor":
    print("name is maor!")
elif name == "moshe":
    print("name is moshe!")
else:
    print("no matching name found")
print("this line runs anyway!")

# ---------------------------------------------------------
# 4. MULTIPLE CONDITIONS (AND / OR)
# 'or' → at least one condition must be True
# 'and' → both conditions must be True
# ---------------------------------------------------------

if name == "maor" or name == "david":
    print("one of the two conditions is true (maor OR david)")
elif name == "maor" and name != "itzik":
    print("name is maor AND name is not itzik")

# ---------------------------------------------------------
# 5. NESTED CONDITIONS
# An 'if' statement inside another 'if'.
# Used when you need to check multiple levels of conditions.
# ---------------------------------------------------------

age = 35
mail = "@gmail.com"

if name == "ron":
    if age == 35 and mail == "@gmail.com":
        print("age is 35, mail is @gmail.com, and name is ron")
    else:
        print("name is ron, but age or mail do not match")
else:
    print("name is not ron!")
