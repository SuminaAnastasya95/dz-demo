age = int(input("Введите ваш возраст: "))

# is_legal_age = False

# if int(age) < 18:
#     is_legal_age = False
# else:
#     is_legal_age = True

# if int(age) > 18:
#     is_legal_age = True


is_legal_age = True if age >= 18 else False
# is_legal_age - то что мы хотим присвоить переменной, 
# True - значение, которое будет подставляться, если условие будет верным if age >= 18,
#else False будет подставляться, если условие (if age >= 18) не верное

print(is_legal_age)    
