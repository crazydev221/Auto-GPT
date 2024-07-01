import string
import secrets


def generate_password(length: int) -> str:
    if length < 8 or length > 16:
        raise ValueError("Password length must be between 8 and 16 characters.")

    characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]
    password += [secrets.choice(characters) for _ in range(length - 4)]
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


if __name__ == "__main__":
    password_length = secrets.SystemRandom().randint(8, 16)
    print(generate_password(password_length))
