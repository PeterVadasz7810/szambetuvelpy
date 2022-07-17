import pytest
from num2text.num2text import szambolbetu


@pytest.mark.parametrize("value", ['test', '5', 't4s', '5rt'])
def test_with_not_number_char(value):
    assert szambolbetu(value) == 'A kapott érték nem egy pozitív egész szám!'


@pytest.mark.parametrize("value", [-99])
def test_with_negative_number(value):
    assert szambolbetu(value) == 'Mínusz kilencvenkilenc'


@pytest.mark.parametrize("value", [50.8, 1.1])
def test_with_decimal_number(value):
    assert szambolbetu(value) == 'A kapott érték nem egy pozitív egész szám!'


@pytest.mark.parametrize("value", [0])
def test_with_zero(value):
    assert szambolbetu(value) == 'Nulla'


@pytest.mark.parametrize("value", [1])
def test_with_the_one(value):
    assert szambolbetu(value) == 'Egy'


@pytest.mark.parametrize("value", [999999999])
def test_with_the_highest_nine_digit_number(value):
    assert szambolbetu(
        value) == 'Kilencszázkilencvenkilencmillió-kilencszázkilencvenkilencezer-kilencszázkilencvenkilenc'


@pytest.mark.parametrize("value", [9999999991])
def test_with_ten_digit_number(value):
    assert szambolbetu(value) == 'A szám túl nagy'
