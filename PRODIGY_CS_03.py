import re

def check_password_strength(password):
    strength = 0
    feedback = ""
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback += "- Password should be at least 8 characters long.\n"
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback += "- Include both uppercase and lowercase letters.\n"
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback += "- Include at least one number.\n"
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback += "- Include at least one special character (e.g., !@#$%^&*).\n"
    if strength >= 5:
        return "Strong password!"
    elif strength >= 3:
        return "Moderate password. Consider improving it.\n" + feedback
    else:
        return "Weak password!\n" + feedback

password = input("Enter a password to check its strength: ")
print(check_password_strength(password))
