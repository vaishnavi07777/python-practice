import string


def check_password(password):
    checks = {
        "Length (8+)": len(password) >= 8,
        "Uppercase": any(c.isupper() for c in password),
        "Lowercase": any(c.islower() for c in password),
        "Digit": any(c.isdigit() for c in password),
        "Special character": any(
            c in string.punctuation for c in password
        ),
    }

    score = sum(checks.values())

    print("\n----- PASSWORD ANALYSIS -----")

    for rule, passed in checks.items():
        status = "Passed" if passed else "Failed"
        print(f"{rule:<20}: {status}")

    if score == 5:
        print("\nStrength: Strong")
    elif score >= 3:
        print("\nStrength: Moderate")
    else:
        print("\nStrength: Weak")


def main():
    password = input("Enter a password: ")
    check_password(password)
