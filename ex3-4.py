# Задание 3
import re


def is_correct_mobile_phone_number_ru(number):
    pattern = r'^(\+7|8)\s?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$'
    return bool(re.match(pattern, number))


def test_is_correct_mobile_phone_number_ru():
    test_cases = [
        ("+7(900)1234567", True),
        ("8(900)1234567", True),
        ("+7 900 1234567", True),
        ("8 900 1234567", True),
        ("+79001234567", True),
        ("89001234567", True),
        ("+7 900 123 45 67", True),
        ("8 900 123 45 67", True),
        ("+7 900-123-45-67", True),
        ("8 900-123-45-67", True),
        ("+7 900-123-45-6", False),
        ("+7 900-123-45-678", False),
        ("8900-123-45-67", False),
        ("+8 900 1234567", False),
        ("7(900)1234567", False),
        ("+7(900)12345", False),
        ("8 (900) 1234-567", False),
        ("+7 900 123 45 678", False),
        ("+7 900-12-45-678", False),
        ("+7 900-123-45-678", False),
    ]

    for number, expected_result in test_cases:
        result = is_correct_mobile_phone_number_ru(number)
        if result == expected_result:
            print(f"Test passed for input '{number}'")
        else:
            print(f"Test failed for input '{number}'")


if __name__ == "__main__":
    test_is_correct_mobile_phone_number_ru()
# Задание 4
import re

def is_correct_mobile_phone_number_ru(number):
    pattern = r'^(\+7|8)\s?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$'
    return bool(re.match(pattern, number))

if __name__ == "__main__":
    input_number = input("Введите номер мобильного телефона: ")
    if is_correct_mobile_phone_number_ru(input_number):
        print("YES")
    else:
        print("NO")
