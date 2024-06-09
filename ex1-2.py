# Задание 1
def is_palindrome(data):
    return data == data[::-1]


def test_is_palindrome():
    test_cases = [
        ("radar", True),
        ("level", True),
        ("noon", True),
        ("python", False),
        ("hello", False),
        ("madam", True)
    ]

    for data, expected_result in test_cases:
        result = is_palindrome(data)
        if result == expected_result:
            print(f"Test passed for input '{data}'")
        else:
            print(f"Test failed for input '{data}'")


if __name__ == "__main__":
    test_is_palindrome()
    # Задание 2
    def is_palindrome(data):
        return data == data[::-1]


    if __name__ == "__main__":
        input_string = input("Введите строку: ")
        if is_palindrome(input_string):
            print("YES")
        else:
            print("NO")
