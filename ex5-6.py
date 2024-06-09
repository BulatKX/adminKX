# Задание 5
import re


def strip_punctuation_ru(data):
    return re.sub(r'[^\w\s]', '', data)


def test_strip_punctuation_ru():
    test_cases = [
        ("Привет, как дела?", "Привет как дела"),
        ("Это. тест! ?", "Это тест"),
        ("Привет!!!", "Привет"),
        ("Тест: знаков препинания нет", "Тест знаков препинания нет"),
        ("Запятая, точка, вопросительный знак?", "Запятая точка вопросительный знак"),
        ("Точка! Точка. Точка...", "Точка Точка Точка"),
        ("Тире - это дефис", "Тире это дефис")
    ]

    for data, expected_result in test_cases:
        result = strip_punctuation_ru(data)
        if result == expected_result:
            print(f"Test passed for input '{data}'")
        else:
            print(f"Test failed for input '{data}'")


if __name__ == "__main__":
    test_strip_punctuation_ru()
# Задание 6
import re

def strip_punctuation_ru(data):
    return re.sub(r'[^\w\s]', '', data)

if __name__ == "__main__":
    input_text = input("Введите текст на русском языке: ")
    result = strip_punctuation_ru(input_text)
    print(result)
