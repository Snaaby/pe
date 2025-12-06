# Руководство пользователя Calculator

## Введение

Calculator — простой калькулятор на Python для базовых математических операций.

**Целевая аудитория:** студенты, разработчики, все кто считает.

## Установка

1. Скачайте репозиторий:
```
git clone https://github.com/Snaaby/pe.git
```

2. Перейдите в папку:
```
cd pe
```

## Использование

### Запуск
```
python calculator.py
```

### Доступные функции

| Функция | Описание | Пример |
|---------|----------|--------|
| add(a, b) | Сложение | add(2, 3) → 5 |
| subtract(a, b) | Вычитание | subtract(5, 2) → 3 |
| multiply(a, b) | Умножение | multiply(4, 3) → 12 |
| divide(a, b) | Деление | divide(10, 2) → 5 |
| square(a) | Квадрат | square(4) → 16 |

### Пример кода
```python
from calculator import add, multiply

result = add(10, 5)
print(result)  # 15

result = multiply(3, 4)
print(result)  # 12
```

## FAQ

**Что будет при делении на ноль?**
Вернётся сообщение: "Ошибка: деление на ноль"

**Как запустить тесты?**
```
python -m pytest test_calculator.py -v
```

## Автор

Констнатин Ч.
