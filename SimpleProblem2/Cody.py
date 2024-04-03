import re

def validate_email(email):
    if len(email) < 3 or len(email) > 20:
        return False
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return False
    return True

email = input("Enter email: ")
if validate_email(email):
    print("Valid email")
else:
    print("Invalid email")
