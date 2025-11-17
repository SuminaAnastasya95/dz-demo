# is_palindrome("А роза упала на лапу Азора")  # → True
# is_palindrome("кот")

is_palindrome = input("Введите слово, для проверки: ")
low_palindrome = is_palindrome.lower()
split_name = "".join(low_palindrome.split(" "))

if split_name == split_name[::-1]:
    print("Это палиндром")
else:
    print("Нет это не палиндром")
