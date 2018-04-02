import snakes_cafe as sc
import pytest as pt


def test_add_item_returns_string():
    # test add_item function is recieving expected input 
    assert sc.current.receipt == {'subtotal': 0}


def test_add_item_adds_single_entry():
    # test add single menue item
    sc.menu = sc.default_menu
    sc.current.add_item('Coffee', 1)
    assert sc.current.receipt == {'subtotal': 1.59, 'Coffee': 1}


def test_add_item_adds_multiple_entries():
    # test add multiple menu items 
    sc.menu = sc.default_menu
    sc.current.add_item('Coffee', 2)
    sc.current.add_item('Coffee', 1)
    sc.current.add_item('Tea', 1)
    assert sc.current.receipt == {'subtotal': 6.36, 'Coffee': 4, 'Tea': 1}


def test_remove_item_test_proper_input():
    # test remove is recieving expected input
    sc.menu = sc.default_menu
    sc.current.add_item('Coffee', 1)
    sc.current.receipt == {'subtotal': 1.59, 'Coffee': 1}


def test_remove_item_test_remove_single_item():
    # test remove is recieving expected input
    sc.menu = sc.default_menu
    sc.current.add_item('Coffee', 2)
    sc.current.remove_item('Coffee', 1)
    sc.current.receipt == {'subtotal': 1.59, 'Coffee': 1}


def test_remove_item_test_remove_multiple_item():
    # test remove is recieving expected input
    sc.menu = sc.default_menu
    sc.current.add_item('Fries', 3)
    sc.current.add_item('Steak', 1)
    sc.current.remove_item('Fries', 2)
    sc.current.receipt == {'subtotal': 3.28, 'Fries': 1, 'Steak': 1}


def test_remove_item_failure():
    """Test removing an item not on the receipt."""
    sc.menu = sc.default_menu
    sc.current.add_item('Steak', 1)
    with pt.raises(Exception):
        sc.current.remove_item('Faygo', 1)


def test_item_add_failure():
    """Test adding an item not on the menu."""
    sc.menu = sc.default_menu
    with pt.raises(Exception):
        sc.current.add_item('Spam Musubi', 1)


def test_len():
    """Test __len__ of receipt."""
    sc.menu = sc.default_menu
    sc.current.add_item('Fries', 3)
    sc.current.add_item('Steak', 1)
    assert sc.current.__len__() == 5


def test_bad_menu():
    """Test exception for giving a bad filetype."""
    with pt.raises(Exception):
        sc.import_menu('test.txt')


def test_invalid_menu_print():
    """Test exception for requesting nonexistant menu."""
    with pt.raises(Exception):
        sc.print_specific('testing')


def test_get_subtotal():
    """Test subtotal calculation."""
    sc.menu = sc.default_menu
    assert sc._get_subtotal('Wings') == 14.31


def test_sales_tax():
    """Test sales tax calculation."""
    assert sc._get_sales_tax(10.00) == 1.01


