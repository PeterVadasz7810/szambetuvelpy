import pytest
from num2text.numberwithtext import NumberWithText, NotANumber, NotAnInteger, TooLargeNumber


@pytest.mark.parametrize("value", ['test', '5', 't4s', '5rt'])
def test_with_not_number_char(value):
    try:
        nt = NumberWithText(value)
        assert False
    except NotANumber:
        assert True


@pytest.mark.parametrize("value", [50.8, 1.1])
def test_with_decimal_number(value):
    try:
        nt = NumberWithText(value)
        assert False
    except NotAnInteger:
        assert True


@pytest.mark.parametrize("value", [10000000000000000000000000000000000000000000000000001])
def test_with_too_large_number(value):
    try:
        nt = NumberWithText(value)
        assert False
    except TooLargeNumber:
        assert True


@pytest.mark.parametrize("value", [-99])
def test_with_negative_number(value):
    nt = NumberWithText(value)
    assert nt.number_with_text == 'mínusz kilencvenkilenc'


@pytest.mark.parametrize("value", [0])
def test_with_zero(value):
    nt = NumberWithText(value)
    assert nt.number_with_text == 'nulla'


@pytest.mark.parametrize("value", [1])
def test_with_the_one(value):
    nt = NumberWithText(value)
    assert nt.number_with_text == 'egy'


@pytest.mark.parametrize("value", [9999999999999999999999999999999999999999999999999999])
def test_with_the_highest_number(value):
    nt = NumberWithText(value)
    assert nt.number_with_text == 'kilencoktilliárd-kilencszázkilencvenkilencoktillió-kilencszázkilencvenkilencszeptilliárd-kilencszázkilencvenkilencszeptillió-kilencszázkilencvenkilencszextilliárd-kilencszázkilencvenkilencszextillió-kilencszázkilencvenkilenckvintilliárd-kilencszázkilencvenkilenckvintillió-kilencszázkilencvenkilenckvadrilliárd-kilencszázkilencvenkilenckvadrillió-kilencszázkilencvenkilenctrilliárd-kilencszázkilencvenkilenctrillió-kilencszázkilencvenkilencbilliárd-kilencszázkilencvenkilencbillió-kilencszázkilencvenkilencmilliárd-kilencszázkilencvenkilencmillió-kilencszázkilencvenkilencezer-kilencszázkilencvenkilenc'
