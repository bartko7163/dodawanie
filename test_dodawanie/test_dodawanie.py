import pytest 
from dodawanie.suma import dodaj, minus

def test_dodawanie():
    assert dodaj(2,4) == 6

def test_minus():
    assert minus(5,6) == 1
