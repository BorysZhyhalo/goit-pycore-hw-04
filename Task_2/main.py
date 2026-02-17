from pathlib import Path
from typing import List, Dict
from pprint import pprint

"""
Аналізує файл cats_file з унікальними даними котів.
Якщо файл відсутній  — повертає пустий список та File is absent! Please upload it!

"""

def get_cats_info(path: Path) -> List[Dict[str, str]]:
    cats: List[Dict[str, str]] = []
    #добввив перевірку на відсутність файлу
    try:
        with open(path, "r", encoding="utf-8") as file:
            for row in file:
                row = row.strip() #видаляємо пробіли і знаки табуляції в кінці рядка
                parts = row.split(",") # розділяємо за комою на три елементи 

                if len(parts) != 3: # перевірка чи наша структура збережена 
                    continue

                cat_id, name, age = parts # розпаковка
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats.append(cat_info)

        return cats

    except FileNotFoundError:
        print("File is absent! Please upload it!")
        return []

cats_info = get_cats_info(Path("Task_2/cats_file.txt"))
pprint(cats_info)

#cats_info = get_cats_info("path/to/cats_file.txt") -> перевірка якщо файлу не має
#print(cats_info)
