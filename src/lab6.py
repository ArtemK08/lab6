"""
Основна програма для Лабораторної роботи № 6.

Цей скрипт повинен імпортувати та використовувати створений вами пакет,
щонайменше один модуль зі стандартної бібліотеки Python,
та щонайменше один сторонній пакет.
"""

# Імпорт зі стандартної бібліотеки Python
import math

# Імпорт стороннього пакета (встановленого через pip)
import requests

# Імпорт функцій з власного пакета geometry_2d
from geometry_2d import rectangle, circle


def main():
    """Основна функція для демонстрації використання модулів та пакетів."""
    print("=== Демонстрація модуля стандартної бібліотеки (math) ===")
    print(f"Квадратний корінь з 16: {math.sqrt(16)}")
    print(f"Значення числа Пі: {math.pi:.4f}\n")

    print("=== Демонстрація стороннього пакета (requests) ===")
    try:
        response = requests.get("https://api.github.com", timeout=10)
        response.raise_for_status()
        print("Успішно підключено до GitHub API.")
    except requests.exceptions.RequestException as e:
        print(f"Не вдалося підключитися до GitHub API: {e}\n")

    print("=== Демонстрація власного пакета geometry_2d ===")

    # Робота з прямокутником
    l, w = 5.0, 3.0
    rect_area = rectangle.area(l, w)
    rect_perim = rectangle.perimeter(l, w)
    print(f"Прямокутник із сторонами {l} та {w}:")
    print(f"  - Площа: {rect_area}")
    print(f"  - Периметр: {rect_perim}")

    # Робота з колом
    r = 4.0
    circ_area = circle.area(r)
    circ_len = circle.circumference(r)
    print(f"\nКоло з радіусом {r}:")
    print(f"  - Площа: {circ_area:.2f}")
    print(f"  - Довжина кола: {circ_len:.2f}")


if __name__ == "__main__":
    main()
