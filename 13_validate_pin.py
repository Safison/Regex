from test_api.checks import run_test, skip_test, format_err_msg
import re

# This challenge is more advanced.
# Again, please do not change the tests
# For the function, delete the `pass` keyword and write code that makes the
#  tests pass


def validate_pin(text):
    """
    Write a function using regex which is going to validate a PIN number. It
    should only contain digits and exactly 4 or 6 of them.

    The function should return True or False.

    For example:
    - 3542 True
    - h23452 False
    - 765609 True
    - ymca False
    - 000432 True
    - 4h537 False
    - 76452 False
    - 1138 True
    - 75500782 False
    """
    pass


@run_test
def test_returns_true_for_valid_pin():
    assert validate_pin("3542"), \
        format_err_msg(True, validate_pin("3542"))
    assert validate_pin("765609"), \
        format_err_msg(True, validate_pin("765609"))
    assert validate_pin("000432"), \
        format_err_msg(True, validate_pin("000432"))


@skip_test
def test_returns_false_for_invalid_pin():
    assert not validate_pin("h23452"), \
        format_err_msg(False, validate_pin("h23452"))
    assert not validate_pin("4k56"), \
        format_err_msg(False, validate_pin("4k56"))
    assert not validate_pin("38462"), \
        format_err_msg(False, validate_pin("38462"))


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == '__main__':
    test_returns_true_for_valid_pin()
    test_returns_false_for_invalid_pin()
