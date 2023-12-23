password = input("Please enter a new password: ")

passwort_strength = {}

def password_checker(password):
    if len(password) >= 12:
        passwort_strength["length"] = True
    else:
        passwort_strength["length"] = False

    digit = False
    for letter in password:
        if letter.isdigit():
            digit = True
    passwort_strength["digits"] = True

    is_upper = False
    for letter in password:
        if letter.isupper():
            is_upper = True
    passwort_strength["is_uppercase"] = is_upper
    print(passwort_strength)

    if all(passwort_strength.values()):
        print("Strong password!")
    else:
        print("Weak password!")


ids = ["XF345_89", "XER76849", "XA454_55"]
 
x = 0
 
for id in ids:
if '_' in id:
    x = x + 1
print(x)