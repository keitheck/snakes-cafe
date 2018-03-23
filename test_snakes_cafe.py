import snakes_cafe as sc
import pytest as pt


def test_add_item_returns_string():
    # test add_item function is recieving expected input 
    assert sc.current.receipt == {'subtotal': 0}
    # import pdb; pdb.set_trace()


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




# def test_item_added():
#     assert sc.item_added(['tea']) == print('1 order of Tea has been added to your meal. Your total is $2.59')


# # def test_get_subtotal():
# #     assert sc.get_subtotal('Tea') == 1.59


# def test_get_sales_tax():
#     assert sc.get_sales_tax(5.00) == .505


# def test_remove_item():
#     assert sc.remove_item('tea') == print('One order of Tea has been removed from your meal. Your total is $0.00')
