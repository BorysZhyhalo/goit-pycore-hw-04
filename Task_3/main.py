from pathlib import Path
from colorama import Fore, Style
import sys


def visualize_directory(path: Path, indent: int = 0) -> None:
    """
    Рекурсивно виводить структуру директорії.
    Папки – синім кольором.
    Файли – зеленим кольором.
    """

    # друкуємо назву директорії лише один раз (кореневу)
    if indent == 0:
        print(Fore.BLUE + f"{path.name}/" + Style.RESET_ALL)

    for item in path.iterdir():
        prefix = " " * indent + "│-- "

        if item.is_dir():
            print(Fore.BLUE + prefix + item.name + "/" + Style.RESET_ALL)
            visualize_directory(item, indent + 4)
        else:
            print(Fore.GREEN + prefix + item.name + Style.RESET_ALL)


def main():
    # Перевірка наявності аргументу
    if len(sys.argv) < 2:
        print("Помилка: потрібно вказати шлях до директорії.")
        print("Приклад: python main.py picture")
        return

    dir_path = Path(sys.argv[1])

    # Перевірка чи існує директорія
    if not dir_path.exists() or not dir_path.is_dir():
        print("Помилка: шлях не існує або це не директорія.")
        return

    visualize_directory(dir_path)


if __name__ == "__main__":
    main()

