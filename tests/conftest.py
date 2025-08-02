import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *
from data import *

@pytest.fixture
def bun():
    return Bun(BUN_NAME_1, BUN_PRICE)

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def ingredient_sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, SAUCE_NAME, SAUCE_PRICE)

@pytest.fixture
def ingredient_filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, FILLING_NAME, FILLING_PRICE)

@pytest.fixture
def database():
    return Database()

# Моки для изолированного тестирования
@pytest.fixture
def mock_bun():
    mock = Mock(spec=Bun)
    mock.get_name.return_value = BUN_NAME_1
    mock.get_price.return_value = BUN_PRICE
    return mock



@pytest.fixture
def mock_sauce():
    return create_mock_ingredient(SAUCE_NAME, SAUCE_PRICE)

@pytest.fixture
def mock_filling():
    return create_mock_ingredient(FILLING_NAME, FILLING_PRICE)

def create_mock_ingredient(name, price):
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = name
    mock.get_price.return_value = price
    return mock