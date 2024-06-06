from test_api.checks import run_test, skip_test, format_err_msg
import re

# This challenge is more advanced.
# Again, please do not change the tests
# For the function, delete the `pass` keyword and write code that makes the
#  tests pass


def match_unique_digits(text):
    """
    Write a function using regex that will return True when the given number
    is composed of unique digits.

    For example:

    - 1234 True
    - 1233 False
    - 493710 True
    - 00 False
    """
    pass


@run_test
def test_match_unique_digits_returns_true_when_number_contains_unique_digits():
    assert match_unique_digits("1234"), \
        format_err_msg(True, match_unique_digits("1234"))
    assert match_unique_digits("493710"), \
        format_err_msg(True, match_unique_digits("493710"))


@skip_test
def test_match_unique_digits_returns_false_when_number_does_not_contain_unique_digits():
    assert not match_unique_digits("1233"), \
        format_err_msg(False, match_unique_digits("1233"))
    assert not match_unique_digits("00"), \
        format_err_msg(False, match_unique_digits("00"))


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == '__main__':
    test_match_unique_digits_returns_true_when_number_contains_unique_digits()
    test_match_unique_digits_returns_false_when_number_does_not_contain_unique_digits()
