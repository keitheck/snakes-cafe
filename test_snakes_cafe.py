import snakes_cafe as sc
# import pytest


def test_add_item_returns_string():
    """
    test add_item function is recieving expected input 
    """
    assert sc.current.receipt == {'subtotal': 0}
    # import pdb; pdb.set_trace()


def test_add_item_adds_single_entry():
    """
    test add single menue item
    """
    sc.menu = sc.default_menu
    sc.current.add_item('Coffee', 1)
    assert sc.current.receipt == {'subtotal': 1.59, 'Coffee': 1}


def test_add_item_adds_multiple_entries():
    """
    test add multiple menu items 
    """
    sc.menu = sc.default_menu
    sc.current.add_item('Coffee', 2)
    sc.current.add_item('Coffee', 1)
    sc.current.add_item('Tea', 1)
    assert sc.current.receipt == {'subtotal': 6.36, 'Coffee': 4, 'Tea': 1}


def test_remove_item_test_proper_input():
    """
    test remove is recieving expected input
    """
    sc.menu = sc.default_menu
    sc.current.add_item('Coffee', 1)
    assert sc.current.receipt == {'Coffee': 5, 'Tea': 1, 'subtotal': 7.95}


def test_remove_item_test_remove_single_item():
    """
    test remove is recieving expected input
    """
    sc.menu = sc.default_menu
    # sc.current.add_item('Coffee', 1)
    sc.current.remove_item('Coffee', 1)
    assert sc.current.receipt == {'Coffee': 4, 'Tea': 1, 'subtotal': 6.36}


def test_remove_item_test_remove_multiple_item():
    """
    test remove is recieving expected input
    """
    sc.menu = sc.default_menu
    sc.current.add_item('Fries', 3)
    sc.current.add_item('Steak', 1)
    sc.current.remove_item('Fries', 2)
    sc.current.receipt == {'subtotal': 3.28, 'Fries': 1, 'Steak': 1}


def test_uuid_created():
    """
    Test is output is a string
    """
    assert type(sc.current.id) == str


def test__len__():
    """
    Returns length of reciept
    """
    sc.menu = sc.default_menu
    sc.current.add_item('Steak', 1)
    assert sc.current.__len__() == 4


def test__repr__():
    """
    Returns repr
    """
    assert type(sc.current.__repr__()) == str


def test_import_menu():
    """
    test that menu is imported
    """
    assert sc.menu != {}


def test_get_subtoatal():
    """
    tests that reciept show correct subtotal
    """
    assert sc.current.receipt['subtotal'] is not None    


def test_get_salestax():
    """
    test if sales tax correctly calculates tax
    """
    assert sc._get_sales_tax(10) == 1.01

