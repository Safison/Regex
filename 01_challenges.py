# Change only the variables called `YOUR_REGEX_HERE`. 
# Please do not adjust any code within the tests. 

import re

def cat(): 
    # Your pattern should **match** a string containing the characters cat
    YOUR_REGEX_HERE = 'x' # <- replace with an appropriate reqular expression pattern
    return re.compile(YOUR_REGEX_HERE) 


def test_cat_matches_correctly():
    assert cat().match('cat').span() == (0, 3)
    assert cat().match('cat11234').group() == 'cat'
    assert not cat().match('asdcatfgh')
    assert not cat().match('Catalogue')
    assert cat().search('cat').group() == 'cat'
    assert cat().search('cat11234').group() == 'cat'
    assert cat().search('asdcatfgh').span() == (3, 6)
    assert not cat().search('Catalogue')
    assert cat().search("asdcat!")
    assert cat().search("36237cat")
    assert not cat().search("ca123")
    assert not cat().search("atasdads")
    assert not cat().search("caasdlkj")
    assert not cat().search("12123ca234")


def at_least_5_digits(): 
    # Your pattern should match a string or substring containing at least 5 of the 
    # digits from 1 to 9 only
    YOUR_REGEX_HERE = 'x' # <- replace with an appropriate reqular expression pattern
    return re.compile(YOUR_REGEX_HERE)


def test_at_least_5_digits_matches_correctly(): 
    assert at_least_5_digits().match("12345")
    assert at_least_5_digits().search("56783")
    assert at_least_5_digits().search("98764").span() == (0, 5)
    assert at_least_5_digits().match("13837").group() == '13837'
    assert at_least_5_digits().match("45613837")
    assert len(at_least_5_digits().findall("45613sggs83767xy")) == 2
    assert at_least_5_digits().search("abc13837def").span() == (3, 8)
    assert at_least_5_digits().search("00abcg77777")
    assert not at_least_5_digits().match("00abcg77777")
    assert at_least_5_digits().search("13837!f")
    assert not at_least_5_digits().search("123")
    assert not at_least_5_digits().search("12308")
    assert not at_least_5_digits().search("1234")
    assert not at_least_5_digits().search("addc6826asd")


def starts_with_exclamation_marks(): 
    # Your pattern should match one or more exclamation marks at the **beginning of a string**
    # You should look up regex anchors for this exercise
    YOUR_REGEX_HERE = 'x' # <- replace with an appropriate reqular expression pattern
    return re.compile(YOUR_REGEX_HERE) 


def test_starts_with_exclamation_marks(): 
    assert starts_with_exclamation_marks().match("!!!sdlasjdlajsd")
    assert starts_with_exclamation_marks().match("!!askjaa").span() == (0, 2)
    assert starts_with_exclamation_marks().match("!!!!!adjaksljd").group() == '!!!!!'
    assert len(starts_with_exclamation_marks().findall("!!!32749!!!anks")) == 1
    assert starts_with_exclamation_marks().match("!abc")

    assert not starts_with_exclamation_marks().match("adssdk!!!")
    assert not starts_with_exclamation_marks().match("asdk;alk!!!!")
    assert not starts_with_exclamation_marks().match("errui!!!!gagahj")
    assert not starts_with_exclamation_marks().match("cjljad!!!!gga!!sdd")


def exact_6_abcs(): 
    # Your pattern should match a string consisting of exactly 6 of a, b or c consecutively
    # You should look up regex anchors for this exercise
    YOUR_REGEX_HERE = 'x' # <- replace with an appropriate reqular expression pattern
    return re.compile(YOUR_REGEX_HERE)


def test_exact_6_abcs(): 
    assert exact_6_abcs().search("abcabc")
    assert exact_6_abcs().match("cbabac")
    assert not exact_6_abcs().search("jdjdhgcacacamzmxm")
    assert not exact_6_abcs().search("bbbccakkksyyt")
    assert not exact_6_abcs().search("xyzxyz") 
    assert not exact_6_abcs().search("pqrsqp")
    assert not exact_6_abcs().search("pprrss")
    assert not exact_6_abcs().search("vsxprh")
    assert not exact_6_abcs().search("abcabca")
    assert not exact_6_abcs().search("abca") 
    assert not exact_6_abcs().search("jdjdhgcacacabmzmxm")
