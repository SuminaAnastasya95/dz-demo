# Задача 4 (по желанию): Объединение конфигов 🔧
# Даны два словаря-конфига:
default_config = {"host": "localhost", "port": 8080, "debug": False}
user_config = {"port": 3000, "debug": True}

# Объедини их так, чтобы user_config переопределял значения из default_config.

# Ожидаемый результат:
# {"host": "localhost", "port": 3000, "debug": True}

# 💡 Подсказка:

# можно вручную: final = default_config.copy(); final.update(user_config)
# или в Python 3.9+: final = default_config | user_config


final = default_config.copy()
final.update(user_config)

print(final)

try_like = default_config | user_config
print(try_like)
