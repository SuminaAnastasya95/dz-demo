import random
import string


def generation_pass(length: int = 8, use_symbols: bool = True):
    if length < 3:
        return ""
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()_+?"
    pool = letters + digits + (symbols if use_symbols else "")

    password_chars: list[str] = []
    while len(password_chars) < length:
        password_chars.append(random.choice(pool))
    return "".join(password_chars)


print(generation_pass())
print(generation_pass(10, False))


def f(a=1, b=2):
    return a*b


print(f(3))
