import snakes_cafe as sc
import pytest as pt


def test_item_added():
    assert sc.item_added(['tea']) == print('1 order of Tea has been added to your meal. Your total is $2.59')


# def test_get_subtotal():
#     assert sc.get_subtotal('Tea') == 1.59


def test_get_sales_tax():
    assert sc.get_sales_tax(5.00) == .505


def test_remove_item():
    assert sc.remove_item('tea') == print('One order of Tea has been removed from your meal. Your total is $0.00')
