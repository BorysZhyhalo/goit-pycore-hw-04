from pathlib import Path
from typing import Tuple, Optional

def total_salary(path: str) -> Tuple[Optional[int], Optional[int]]:
    """
    Аналізує файл salary_file із зарплатами та повертає кортеж.
    Якщо файл відсутній або немає валідних даних — повертає (None, None).
    """

    try:
        total: int = 0     # накопичена сума зарплат
        count: int = 0     # кількість валідних записів

        # Відкрити файл у контекстному менеджері
        with open(path, "r", encoding="utf-8") as file:

            # Пройтись по кожному рядку
            for row in file:
                row = row.strip()

                # Пропускаємо пусті рядки
                if not row:
                    continue

                # Розділити рядок на дві частини: ім'я і зарплата 
                parts = row.split(",")

                # Має бути рівно дві частини: -> name and raw_salary
                if len(parts) != 2:
                    continue

                name = parts[0].strip() 
                raw_salary = parts[1].strip()

                # Перевірка ім'я не пусте
                if not name:
                    continue

                # Перевірка зарплати: тільки цифри
                if not raw_salary.isdigit():
                    continue

                salary = int(raw_salary)

                # Зарплата має бути позитивною
                if salary <= 0:
                    continue

                # Накопичення результатів
                total += salary
                count += 1

        # Якщо не було валідних записів
        if count == 0:
            return None, None

        # Середня зарплата
        average = total // count

        return total, average

    except FileNotFoundError:
        print("File is absent! Please upload it!")
        return None, None

total, average = total_salary(Path("Task_1/salary_file.txt"))
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")