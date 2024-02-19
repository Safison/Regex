import pytest

# These challenges are more advanced.
# Again, please do not change the tests
# For each function, delete the `pass` keyword and write code that makes the
#  tests pass


def extract_code(text):
    """
    This function should take a string as an argument

    Somewhere in the middle of the string, there will be a series of
    consecutive digits composing a number

    You should extract that number from the string and return it
    """
    pass


def test_extract_code_finds_number_in_single_word_string():
    assert extract_code("abcd67yuio") == 67
    assert extract_code("abcd103yuio") == 103
    assert extract_code("abcd4567yuio") == 4567
    assert extract_code("abcd1000289yuio") == 1000289


def is_valid_sort_code(text):
    """
    This function should take a string representing a sort code as an argument

    A valid sort code should adhere to the format: 2 digits hyphen 2 digits
    hyphen 2 digits

    You should return True if the sort code is valid, and False otherwise
    """
    pass


@pytest.mark.skip()
def test_is_valid_sort_code_checks_sort_code_in_the_correct_format():
    assert is_valid_sort_code("10-34-67")
    assert is_valid_sort_code("51-34-58")
    assert is_valid_sort_code("85-16-23")
    assert not is_valid_sort_code("51-349-67")
    assert not is_valid_sort_code("7980-34-67")
    assert not is_valid_sort_code("34-12-899")
    assert not is_valid_sort_code("a8-78-10")
    assert not is_valid_sort_code("45_78_10")


def is_professional_email(text):
    """
    This function should take a string representing an email as an argument

    An email is considered to be professional if it does not end with a kiss
    ("x" or "X")

    You should return True if the email is professional, and False otherwise
    """
    pass


@pytest.mark.skip()
def test_is_professional_email_checks_if_email_ends_with_x():
    assert not is_professional_email("x")
    assert is_professional_email("Dear Sir/Madam")
    assert is_professional_email("Dear Alex, How are you?")
    assert not is_professional_email("i miss u xx")
    assert not is_professional_email("X_X")


def count_vowels(text):
    """
    This function should take a string as an argument, and return a count
    representing the number of vowels it contains
    """
    pass


@pytest.mark.skip()
def test_count_vowels_counts_vowels_in_string():
    assert count_vowels("") == 0
    assert count_vowels("bcd") == 0
    assert count_vowels("a") == 1
    assert count_vowels("abc") == 1
    assert count_vowels("AEbiO") == 4
    assert count_vowels("aaeee!!!") == 5


def sum_nums(text):
    """
    This function should take a string as an argument, and return a sum of
    all the numbers found within.

    Consecutive digits should be taken as numbers: i.e. "24" = 24, not 6

    If there are no numbers, you should return 0
    """
    pass


@pytest.mark.skip()
def test_sum_nums_totals_all_numbers_in_string():
    assert sum_nums("hello") == 0
    assert sum_nums("1") == 1
    assert sum_nums("12") == 12
    assert sum_nums("1hello2") == 3
    assert sum_nums("12hiya!3") == 15


def is_valid_countdown(text):
    """
    This function should take a string as an argument

    The function must return a boolean depending on if the string is a valid
    collection of letters for the TV show countdown.

    In countdown a valid collection contains at least 4 consonants and 3
    vowels and has exactly 9 letters
    """
    pass


@pytest.mark.skip()
def test_is_valid_countdown_correctly_detects_valid_combinations():
    # >=4 consonants, >=3 vowels, exactly 9 letters
    assert is_valid_countdown("aaabbbccc")
    assert is_valid_countdown("eeeedddff")
    assert is_valid_countdown("aeiouwxyz")
    assert is_valid_countdown('abejikosu')
    assert not is_valid_countdown("aeiouaxyz")
    assert not is_valid_countdown("aabbbcccd")
    assert not is_valid_countdown("aeiouvwxyz")
    assert not is_valid_countdown("aaaaaaaaa")
    assert not is_valid_countdown("bbbbbbbbb")
    assert not is_valid_countdown('aaaabbbb')


def extract_repo_name(text):
    """
    This function should take a string representing a github url and return
    the name of the repo.

    Github urls are of the form https://github.com/northcoders/intro-week
    where "northcoders" is the name of the account and "intro-week" is the
    name of the repo
    """
    pass


@pytest.mark.skip()
def test_extract_repo_name_returns_repo_name():
    assert extract_repo_name(
        "https://github.com/northcoders/intro-week") == "intro-week"
    assert \
        extract_repo_name(
            "https://github.com/northcoders/remote-git-workshop") \
        == "remote-git-workshop"
    assert extract_repo_name("https://github.com/myAccount/notes") == \
        "notes"
    assert extract_repo_name("https://github.com/myAccount/notes/settings") \
        == "notes"


def has_exactly_2_consecutive_ls(text):
    """
    This function should take a string as an argument

    You will need to check whether or not it contains *exactly* 2 consecutive
    occurrences of the letter "l" (lower case)

    This means that there *must* be exactly 2 "l"s in total and they *must* be
    consecutive

    You should return True if this is the case, and False otherwise
    """
    pass


@pytest.mark.skip()
def test_has_exactly_2_consecutive_ls_identifies_occurrences_correctly():
    assert has_exactly_2_consecutive_ls("ll")
    assert has_exactly_2_consecutive_ls("hello")
    assert has_exactly_2_consecutive_ls("bells")
    assert has_exactly_2_consecutive_ls("bellows")
    assert has_exactly_2_consecutive_ls("aaaallasdows")
    assert has_exactly_2_consecutive_ls("llama")
    assert has_exactly_2_consecutive_ls("well")

    assert not has_exactly_2_consecutive_ls("mile")
    assert not has_exactly_2_consecutive_ls("fly")
    assert not has_exactly_2_consecutive_ls("wellll")
    assert not has_exactly_2_consecutive_ls("mitchelllloyd")
    assert not has_exactly_2_consecutive_ls("l")


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


@pytest.mark.skip()
def test_validate_pin_correctly_identifies_valid_pins():
    assert validate_pin("3542")
    assert validate_pin("765609")
    assert not validate_pin("h23452")
    assert validate_pin("000432")
    assert not validate_pin("4k56")
    assert not validate_pin("38462")


def spot_the_contraction(text):
    """
    Write a function using regex to return True if a sentence contains any of
    these contractions: "I'm", "I've" or "don't". (case insensitive)

    This function will take a string and return True or False. See examples
    below:

    - "do not" False
    - "don't" True
    - "I am" False
    - I have been fishing and I've caught plenty fishes True
    - "I am a coding panda" False
    - "I'm a coding panda" True
    - I've got a collection of foreign coins True
    - "Sometimes I do not like to get up early" False
    - "Sometimes I don't like to get up early" True
    - "Don't feed the birds" True
    """
    pass


@pytest.mark.skip()
def test_spot_the_contraction_spots_contractions():
    assert not spot_the_contraction("do not")
    assert not spot_the_contraction("I am")
    assert not spot_the_contraction("I am a coding panda")
    assert not spot_the_contraction("Sometimes I do not like to get up early")

    assert spot_the_contraction("I am a vampire and I don't drink water")

    assert not spot_the_contraction("I have been fishing")
    assert spot_the_contraction("I've got a collection of foreign coins")


def exclude_words(text):
    """
    Write a function using regex which returns a string with everything except
    the words 'north' and 'coders'.

    Everything else, even words starting, including or ending with these words
    should be matched.

    Your matches and non-matches should be case insensitive.

    For example:
    - "I visited the north pole last year." should be "I visited the pole last
        year."
    - "I study at Northcoders." should be "I study at Northcoders."
    - "IBM hired a lot of coders." should be "IBM hired a lot of ."
    """
    pass


@pytest.mark.skip()
def test_exclude_words_excludes_separate_words_only():
    assert exclude_words(
        "I visited the north pole last year") == "I visited the pole last year"
    assert exclude_words("I study at Northcoders") == "I study at Northcoders"
    assert exclude_words(
        "IBM hired a lot of coders lately") == "IBM hired a lot of lately"


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


@pytest.mark.skip()
def test_match_unique_digits_identifies_numbers_with_unique_digits():
    assert match_unique_digits("1234")
    assert not match_unique_digits("1233")
    assert match_unique_digits("493710")
    assert not match_unique_digits("00")
