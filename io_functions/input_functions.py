from typing import List

def get_option_from_list(options: List[str]) -> str:
    for index, option in enumerate(options):
        print(f"{[index]} {option}")
    try:
        option_index = int(input("[choice_index] > "))
        return options[option_index]
    except IndexError:
        print(f"Option {option_index} Invalid Index. Choose from:")
        get_option_from_list(options)
    except ValueError:
        print(f"Option {option_index} Invalid Value. Choose from:")
        get_option_from_list(options)


def get_yes_no_bool() -> bool:
    valid_options = ["y", "yes", "n", "no"]
    choice = input("Yes/No? > ").lower()
    if choice not in valid_options:
        print("Option invalid. Choose from: y | n")
        get_yes_no_bool()
    
    if choice in valid_options[:2]:
        return True
    return False
