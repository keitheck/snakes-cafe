import uuid
import csv
import sys

menu = {}

default_menu = {
    'appetizers': {'Wings': 1.59,
                   'Cookies': 1.59,
                   'Spring Rolls': 1.59,
                   'Fries': 1.59,
                   'Pickles': 1.59,
                   'Onion Rings': 1.59,
                   'Quesadilla': 1.59,
                   'Mini Pizzas': 1.59,
                   'Artichoke Dip': 1.59
                   },
    'entrees': {'Salmon': 1.59,
                'Steak': 1.59,
                'Meat Tornado': 1.59,
                'A Literal Garden': 1.59,
                'Chicken': 1.59,
                'Sushi': 1.59,
                'Burger': 1.59,
                'Turf n Turf': 1.59,
                'Turducken': 1.59,
                'Quail': 1.59
                },
    'desserts': {'Ice Cream': 1.59,
                 'Cake': 1.59,
                 'Pie': 1.59,
                 'Froyo': 1.59,
                 'Flan': 1.59,
                 'Creme Brulee': 1.59,
                 'Chocolate Mousse': 1.59,
                 'Chocolate Moose': 1.59,
                 'Chocolate Mouse': 1.59
                 },
    'drinks': {'Coffee': 1.59,
               'Tea': 2.59,
               'Blood Of The Innocent': 1.59,
               'Water': 1.59,
               'Beer': 1.59,
               'A Larger Beer': 1.59,
               'Bubble Tea': 1.59,
               'Faygo': 1.59,
               'Red Bull': 1.59
               },
    'sides': {'Tiny Salad': 1.59,
              'Cup Soap': 1.59,
              'Fruit Bowl': 1.59,
              'Fried Okra': 1.59,
              'Bacon': 1.59,
              'Giant Beer': 1.59,
              'Just Carbs': 1.59,
              'Potato Volcano': 1.59,
              'Carrots': 1.59
              }
}
# Write menu to csv file

# with open('menu_two.csv', 'w') as csv_file:
#     csv_menu = csv.writer(csv_file, delimiter=',')
#     for category in menu_two:
#         for item in menu_two[category]:
#             csv_menu.writerow([category, item, menu_two[category][item]])
# menu_two = {}


def import_menu(file_path):
    with open(file_path, 'r') as f:
        menu_import = csv.reader(f)
        for row in menu_import:
            item = iter(row[1:])
            # import pdb; pdb.set_trace()
            if row[0] in menu.keys():
                menu[row[0]].update(dict(zip(item, item)))
            else:       
                menu[row[0]] = dict(zip(item, item))
        print_menu(menu)        


def what_menu():
    print('Would you like to import a menu?')
    menu_choice = input('> ')
    try:
        if menu_choice.lower() == 'yes':
            print('What is the filepath?')
            filepath = input('> ')
            import_menu(filepath)
        else:
            global menu
            menu = default_menu
            print_menu(menu)
    except TypeError:
        print('invalid input. Enter yes or no')           


receipt = {'subtotal': 0,
           'order_id': uuid.uuid4().hex
           }

subtotal = 0


# def print_specific(order):
#     print(order)
#     print('-' * 8)
#     for key, value in menu[order].items():
#         print(key.ljust(50), '$' + str(value))
#     print('\n')


def print_apps(dict):
    """
    This function prints appetizers.
    """
    print('Appetizers')
    print('-' * 8)
    for key, value in dict['appetizers'].items():
        print(key.ljust(50), '$' + str(value))
    print('\n')


def print_entrees(dict):
    """
    This function prints entrees.
    """
    print('Entrees')
    print('-' * 8)
    for key, value in dict['entrees'].items():
        print(key.ljust(50), '$' + str(value))
    print('\n')


def print_sides(dict):
    """
    This function prints sides.
    """
    print('Sides')
    print('-' * 8)
    for key, value in dict['sides'].items():
        print(key.ljust(50), '$' + str(value))
    print('\n')


def print_desserts(dict):
    """
    This function prints desserts.
    """
    print('Desserts')
    print('-' * 8)
    for key, value in dict['desserts'].items():
        print(key.ljust(50), '$' + str(value))
    print('\n')


def print_drinks(dict):
    """
    This function prints drinks.
    """
    print('Drinks')
    print('-' * 8)
    for key, value in dict['drinks'].items():
        print(key.ljust(50), '$' + str(value))
    print('\n')


def print_menu(dict):
    """
    This function prints the whole menu.
    """
    print('***************************************')
    print('**    Welcome to the Snakes Cafe!    **')
    print('**    Please see our menu below.     **')
    print('**                                   **')
    print('**  To quit at any time, type "quit" **')
    print('***************************************')
    print_apps(dict)
    print_entrees(dict)
    print_sides(dict)
    print_desserts(dict)
    print_drinks(dict)
    print('***************************************')
    print('**   What would you like to order?   **')
    print('***************************************')


def get_subtotal(order):
    """
    This function gets the subtotal of all purchased items.
    """
    for key, value in menu.items():
        if order in menu[key]:
            receipt['subtotal'] += menu[key][order]
    return round(receipt['subtotal'], 2)


def get_sales_tax(subtotal):
    """
    This function calculates sales tax.
    """
    tax = subtotal * 0.101
    return tax


def item_added(order):
    """
    This function handles adding items to the order.
    """
    # print('order %s' % order)
    flag = False
    # print(menu)
    for key, value in menu.items():
        if order in menu[key]:
            flag = True
            if order in receipt:
                receipt[order] += 1
                total = get_subtotal(order)
                print(f'{receipt[order]} orders of {order} have been added to your meal. Your total is ${total}')
            else:
                receipt[order] = 1
                total = get_subtotal(order)
                print(f'One order of {order} has been added to your meal. Your total is ${total}')
    if flag is False:
        print('That\'s not on the menu!')


def remove_item(order):
    """
    This function handles removing items from the order.
    """
    delete_item = order.split(' ')
    delete_item = ' '.join(delete_item[1:])
    for key, value in menu.items():
        try:
            if delete_item in menu[key]:
                receipt['subtotal'] -= menu[key][delete_item]
                if receipt[delete_item] == 1:
                    del receipt[delete_item]
                else:
                    receipt[delete_item] -= 1
                total = receipt['subtotal']
                print(f'One order of {delete_item} has been removed from your meal. Your total is ${total}')
        except KeyError:
            print('Oops! You don\'t have one of those on your receipt.')


def calculate_line_item(item):
    """
    This function gets each line item and its cost.
    """
    for key, value in menu.items():
        if item in menu[key]:
            unit_cost = menu[key][item]
            item_name = item
            return(item_name, unit_cost)


def print_receipt(receipt):
    """
    This function prints the final receipt.
    """
    tax = round(get_sales_tax(receipt['subtotal']), 2)
    print('*' * 50)
    print('The Snakes Cafe')
    print('"Eatability Counts"')
    print('Order', receipt['order_id'])
    print('=' * 50)
    for key, value in receipt.items():
        unit_cost = calculate_line_item(key)
        if unit_cost is not None:
            print(unit_cost[0].ljust(40), '$', unit_cost[1] * receipt[key])
    print('-' * 50)
    print('Subtotal'.ljust(40), '$', receipt['subtotal'])
    print('Sales Tax'.ljust(40), '$', tax)
    print('-' * 10)
    print('Total Due'.ljust(40), '$', str(round(receipt['subtotal'] + tax)), 2)
    print('*' * 50)


def main():
    """
    This function triggers the app.
    """
    what_menu()

    while True:
        order = input('> ').lower()
        if order == 'quit':
            exit()

        elif order == 'menu':
            print('\n')
            print_menu()

        elif order == 'appetizers':
            print('\n')
            print_apps()

        elif order == 'entrees':
            print('\n')
            print_entrees()

        elif order == 'sides':
            print('\n')
            print_sides()

        elif order == 'desserts':
            print('\n')
            print_drinks()

        elif order == 'drinks':
            print('\n')
            print_drinks()

        elif order == 'order':
            print_receipt(receipt)

        elif order.split(' ').pop(0) == 'remove':
            remove_item(order.title())

        else:
            item_added(order.title())


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Thanks for your order!')
