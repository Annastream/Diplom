import pytest
from data import *
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, SAUCE_NAME, SAUCE_PRICE),
        (INGREDIENT_TYPE_FILLING, FILLING_NAME, FILLING_PRICE)
])
class TestIngredients:

    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price, f"Цена ингредиента {ingredient.get_price()} не соответствует ожидаемой {price}"



    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name, f"Название ингредиента '{ingredient.get_name()}' не соответствует ожидаемому '{name}'"

    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type, f"Тип ингредиента '{ingredient.get_type()}' не соответствует ожидаемому '{ingredient_type}'"