# 07_02_2026_packed_exe

Калькулятор замовлень / Order Calculator

## Описание / Description

Програма для введення та розрахунку даних замовлень з наступними полями:
Program for entering and calculating order data with the following fields:

- **Номер_Заказа** (Order Number)
- **Материал** (Material)
- **Лот** (Lot)
- **Ширина** (Width)
- **Длина** (Length)
- **Толщина** (Thickness)
- **Вес_коробки** (Box Weight)
- **Колич** (Quantity)
- **Бонус** (Bonus) - рассчитывается как: Quantity × Length

## Возможности / Features

✅ Введение данных замовлення (Input order data)
✅ Автоматический расчет бонуса (Automatic bonus calculation)
✅ Сохранение истории заказов в JSON (Save order history to JSON)
✅ Просмотр истории (View order history)
✅ Двуязычный интерфейс (Bilingual interface - Ukrainian/Russian & English)

## Использование / Usage

```bash
python Main/main.py
```

## Требования / Requirements

- Python 3.6+
- tkinter (встроено в Python на Windows / built-in with Python on Windows)

## Структура проекта / Project Structure

```
07_02_2026_packed_exe/
├── Main/
│   └── main.py          # Главная программа / Main application
├── History/             # Папка для истории / History folder
└── README.md
```
