from typing import Callable, Dict, List, Tuple
from handlers import add_contact, change_contact, show_phone, show_all


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args

def main() -> None:
    contacts: Dict[str, str] = {}

    commands: Dict[str, Callable[[List[str], Dict[str, str]], str]] = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
    }

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in {"close", "exit"}:
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")
            continue

        handler = commands.get(command)

        if handler:
            result = handler(args, contacts)
            print(result)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


