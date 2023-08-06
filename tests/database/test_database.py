import pytest


@pytest.mark.database
def test_database_connection(database):
    database.test_connection()


@pytest.mark.database
def test_check_all_users(database):
    users = database.get_all_users()
    print(users)


@pytest.mark.database
def test_check_user_sergii(database):
    user = database.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update(database):
    database.update_product_qnt_by_id(1, 25)
    water_qnt = database.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert(database):
    database.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = database.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete(database):
    database.insert_product(99, 'тестові', 'дані', 999)
    database.delete_product_by_id(99)
    qnt = database.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders(database):
    orders = database.get_detailed_orders()
    print("Замовлення", orders)
    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'


@pytest.mark.database
def test_incorrect_data_insert(database):
    database.insert_incorrect_datatype(4, 'томат', 'червоний', False)
    products = database.select_product_with_incorrect_data_by_id(4)
    assert products[0][3] == 0


@pytest.mark.database
def test_is_value_integer(database):
    data = database.is_value_integer(2)
    assert data


@pytest.mark.database
def test_add_new_customer(database):
    data = database.select_all_customers_from_database()
    database.insert_new_customer('Vlad', 'Chornovola, 17', 'Lviv', 4224, 'Ukraine')
    new_data = database.select_all_customers_from_database()
    assert data[-1][0] + 1 == new_data[-1][0]


@pytest.mark.database
def test_sum_of_one_product(database):
    products_quantity = database.select_quantity_by_name('солодка вода')
    sum_of_products = 0
    for i in products_quantity:
        sum_of_products += i[0]
    assert sum_of_products == 35

@pytest.mark.database
def test_unique_of_id(database):
    data = database.insert_product(101, 'ковбаса', 'салямі', 4)
    new_data = database.insert_product(101, 'сосиски', 'баварські', 12)
    db = database.select_product_by_id(101)
    assert db[0][0] == 100
    assert db[0][1] == 'сосиски'
    assert db[0][2] == 'баварські'
    assert db[0][3] == 12
