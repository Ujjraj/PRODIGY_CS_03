# PASSWORD COMPLEXITY CHECKER

## DESCRIPTION

A beginner-friendly Python tool that evaluates the strength of a password based on key security criteria such as length, uppercase/lowercase letters, numbers, and special characters. It also provides feedback on how to improve weak passwords.


## How Does It Work?

#### *The script follows these steps:*
1. Accepts user input (password).
2. Checks for strength criteria (length, letters, numbers, special characters).
3. Calculates a strength score and provides feedback.
4. Displays the result as "Strong," "Moderate," or "Weak".

---

### Example Outputs

```
Enter a password to check its strength: Ujjawal
Weak password!
- Password should be at least 8 characters long.
- Include at least one number.
- Include at least one special character (e.g., !@#$%^&*).
```

---
```
Enter a password to check its strength: Ujjawal2003
Moderate password. Consider improving it.
- Include at least one special character (e.g., !@#$%^&*).
```

---
```
Enter a password to check its strength: Ujjawal2003@
Strong password!
```
