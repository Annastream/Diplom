import pytest
from praktikum.database import Database
from data import *


class TestDatabase:
   # Проверка доступных булок для бургера
    @pytest.mark.parametrize('name,price,index', BUN_LIST)
    def test_available_buns(self, name, price, index):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3
        assert (buns[index].get_name() == name and
               buns[index].get_price() == price)


    #Проверка доступных ингредиентов для бургера
    @pytest.mark.parametrize('type_ingredient,name,price,index', INGREDIENT_LIST)
    def test_available_ingredients(self, type_ingredient, name, price, index):
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert (ingredients[index].get_type() == type_ingredient and
                ingredients[index].get_name() == name and
                ingredients[index].get_price() == price)