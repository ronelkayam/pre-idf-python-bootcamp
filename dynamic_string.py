# ---------------------------------------------------------
# Dynamic Strings in Python
# Full examples with English explanations
# ---------------------------------------------------------

# Dynamic strings allow us to insert variables into text.
# Python gives us several ways to do this.

name = "Ron"
age = 35
mail = "ron@gmail.com"

# ---------------------------------------------------------
# 1. f-strings (Recommended)
# Introduced in Python 3.6
# Fast, clean, and easy to read.
# ---------------------------------------------------------

print(f"Hello, my name is {name} and I am {age} years old.")
print(f"My email address is {mail}")

# You can also do calculations inside an f-string:
print(f"In 10 years, I will be {age + 10} years old.")

# ---------------------------------------------------------
# 2. format() method
# Older method, still common in some codebases.
# ---------------------------------------------------------

print("Hello, my name is {} and my age is {}".format(name, age))
print("My email is: {}".format(mail))

# You can also specify positions:
print("Age: {1}, Name: {0}".format(name, age))  # switches order

# ---------------------------------------------------------
# 3. %-formatting (Very old style)
# Not recommended today, but still works.
# ---------------------------------------------------------

print("Hello, my name is %s and I am %d years old." % (name, age))

# ---------------------------------------------------------
# 4. Building dynamic strings using concatenation
# Not recommended for long or complex strings.
# ---------------------------------------------------------

print("My name is " + name + " and my email is " + mail)

# ---------------------------------------------------------
# 5. Multi-line dynamic strings (f-string + triple quotes)
# Useful for long text like messages or templates.
# ---------------------------------------------------------

message = f"""
Hello {name},

Your account information:
- Age: {age}
- Email: {mail}

Thank you for joining us!
"""

print(message)

# ---------------------------------------------------------
# 6. Dynamic string with dictionary or object
# Using f-strings with keys or attributes
# ---------------------------------------------------------

user = {
    "name": "Ron",
    "age": 35,
    "mail": "ron@gmail.com"
}

print(f"User: {user['name']}, Age: {user['age']}, Mail: {user['mail']}")

# ---------------------------------------------------------
# 7. Formatting numbers dynamically
# f-strings allow formatting numbers easily
# ---------------------------------------------------------

price = 1234.56789
print(f"Price: {price:.2f}")   # 2 decimal places
print(f"Price with commas: {price:,.2f}")  # formatted number

# ---------------------------------------------------------
# End of Dynamic String Examples
# ---------------------------------------------------------
