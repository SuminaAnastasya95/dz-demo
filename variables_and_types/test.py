# Описание: Реализуйте функцию, которая принимает число и возвращает его тип в виде строки.
# Входные данные: value: любое значение (int, float, str, bool)
# Выходные данные: строка с названием типа данных
# Ограничения: Входное значение может быть любым из базовых типов Python
# Примеры:
# Input: 42
# Output: "int"
# Input: 3.14
# Output: "float"

def get_type_name(value):
    return type(value).__name__

#Как задается функция
# def get_type_name(value):
#     # Ваш код здесь
#     return # Вернуть название типа

# Атрибут __name__ возвращает имя класса в виде строки.
# print(type(42).__name__)      # "int"
# print(type(3.14).__name__)    # "float" 
# print(type("hello").__name__) # "str"
