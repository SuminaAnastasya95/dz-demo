pasword = 'hello, purpleSchool ! '
print(pasword.upper()) #верхний регистр
print(pasword.capitalize()) #первая буква большая
print(pasword.lower()) #нижний регистр
print(pasword.strip()) #удаляет проблемы после
print(pasword.replace("p", "j")) #заменя символов
print(pasword.split(","))

multiline = """Line1 
Line2
Line3"""
print(multiline.splitlines()) #Разбиение строк на отдельные значения в список