from data import *
class TestBurger:

# проверка добавления одного ингредиента (соуса)
    def test_add_one_ingredient(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        assert burger.ingredients[0].get_name() == SAUCE_NAME, "Ингредиент  добавлен некорректно"
# проверка добавления двух разных ингредиентов (соус и начинка)
    def test_add_two_ingredients(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.ingredients[0].get_name() == SAUCE_NAME and burger.ingredients[1].get_name() == FILLING_NAME, "Ингредиенты добавлены некорректно"

# проверяет корректность удаления ингредиента по индексу
    def test_remove_ingredient(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(1)
        assert burger.ingredients[0].get_name() == SAUCE_NAME and len(
            burger.ingredients) == 1, "Ингредиент удален некорректно"
# Проверяется корректность изменения порядка ингредиентов
    def test_move_ingredient(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0].get_name() == FILLING_NAME and burger.ingredients[1].get_name() == SAUCE_NAME
        assert len(burger.ingredients) == 2, "Ингредиент  перемещен некорректно"

# проверяет правильность расчета общей стоимости бургера
    def test_get_price(self, burger, mock_bun, mock_sauce, mock_filling):
        mock_bun.get_price.return_value = BUN_PRICE
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        expected_price = BUN_PRICE * 2 + SAUCE_PRICE + FILLING_PRICE
        assert burger.get_price() == expected_price, f"Стоимость бургера {burger.get_price()} не соответствует ожидаемой {expected_price}"


def test_get_receipt( burger, mock_bun, mock_sauce, mock_filling):
    # Настраиваем дополнительные возвращаемые значения для моков
    mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING

    # Собираем бургер
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_sauce)
    burger.add_ingredient(mock_filling)

    # Формируем ожидаемый чек
    expected_receipt = (
        f"(==== {BUN_NAME_1} ====)\n"
        f"= {INGREDIENT_TYPE_SAUCE.lower()} {SAUCE_NAME} =\n"
        f"= {INGREDIENT_TYPE_FILLING.lower()} {FILLING_NAME} =\n"
        f"(==== {BUN_NAME_1} ====)\n"
        f"\nPrice: {BUN_PRICE * 2 + SAUCE_PRICE + FILLING_PRICE}"
    )

    # Проверяем
    assert burger.get_receipt() == expected_receipt