"""
Юніт-тести для Лабораторної роботи № 6.

Студенти повинні доповнити цей файл тестами для своїх рішень.
"""
import unittest
import sys
import os

# Додаємо шлях до src, щоб тести бачили пакет geometry_2d
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from geometry_2d import rectangle, circle


class TestGeometry2D(unittest.TestCase):
    """Клас для тестування геометричних функцій."""

    def test_rectangle_area(self):
        """Тест обчислення площі прямокутника."""
        self.assertEqual(rectangle.area(4, 5), 20)
        self.assertEqual(rectangle.area(2.5, 4), 10.0)
        self.assertEqual(rectangle.area(0, 10), 0)

    def test_rectangle_perimeter(self):
        """Тест обчислення периметра прямокутника."""
        self.assertEqual(rectangle.perimeter(4, 5), 18)
        self.assertEqual(rectangle.perimeter(2.5, 3.5), 12.0)

    def test_rectangle_exceptions(self):
        """Перевірка викидання винятків для некоректних даних прямокутника."""
        with self.assertRaises(ValueError):
            rectangle.area(-3, 5)
        with self.assertRaises(ValueError):
            rectangle.perimeter(4, -1)

    def test_circle_area(self):
        """Тест обчислення площі кола."""
        self.assertAlmostEqual(circle.area(3), 28.27433388, places=5)
        self.assertEqual(circle.area(0), 0)

    def test_circle_circumference(self):
        """Тест обчислення довжини кола."""
        self.assertAlmostEqual(circle.circumference(3), 18.84955592, places=5)

    def test_circle_exceptions(self):
        """Перевірка викидання винятків для некоректних даних кола."""
        with self.assertRaises(ValueError):
            circle.area(-5)
        with self.assertRaises(ValueError):
            circle.circumference(-2.5)


if __name__ == '__main__':
    unittest.main()
