name, email, age = "Anastasya", "a@a.ru", 15
print("Hi " + name + " your email is " + email + " and your age is " + str(age))

print("_"*50)
print("hi {} with {}, age - {}".format(name, email, age))

print("_"*50)
print("hi {n} with {e}, age - {a}".format(n=name, e=email, a=age))
# Самый оптимальны вывод данныхв строках
print("_"*50)
print(f"Hi {name} with email {email} and age {age:.1f}")