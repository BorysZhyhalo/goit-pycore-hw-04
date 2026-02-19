from typing import List, Dict


def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 2:
        return "Please provide name and phone"

    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 2:
        return "Please provide name and phone"

    name, phone = args

    if name in contacts:
        contacts[name] = phone
        return "Contact updated."

    return "Contact not found."


def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 1:
        return "Please provide name"

    name = args[0]

    if name in contacts:
        return contacts[name]

    return "Contact not found."


def show_all(args: List[str], contacts: Dict[str, str]) -> str:
    if not contacts:
        return "No contacts found."

    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)


