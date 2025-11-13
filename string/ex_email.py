# a@a.ru  - True
# a@.ru - False
# a@.r - False
# a@ru - False
# @a.ru - False
# a@.com - False


email = str(input("Введите свою почту: "))

if email.count("@") != 1:
    print("Почта не корректна, not @")
    exit()

local, domain = email.split("@")
if not local:
    print("Почта не корректна, not local")
    exit()
if not domain:
    print("Почта не корректна, not domain")
    exit()
if "." not in domain:
    print("Почта не корректна, not '.'")
    exit()
if len(domain.split(".") [-1])<2:
    print("Почта не корректна, not correct len domain")
    exit()
if len(domain.split(".") [-0])==0:
    print("Почта не корректна, not name domain, only .ru/com")
    exit()
print("А ты молодец")
