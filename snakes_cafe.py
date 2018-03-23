import uuid
import csv
import sys

menu = {}
categories = ['appetizers', 'entrees', 'drinks', 'desserts', 'sides']
default_menu = {
    'appetizers': {'Wings': [1.59, 5],
                   'Cookies': [1.59, 5],
                   'Spring Rolls': [1.59, 5],
                   'Fries': [1.59, 5],
                   'Pickles': [1.59, 5],
                   'Onion Rings': [1.59, 5],
                   'Quesadilla': [1.59, 5],
                   'Mini Pizzas': [1.59, 5],
                   'Artichoke Dip': [1.59, 5]
                   },
    'entrees': {'Salmon': [1.59, 5],
                'Steak': [1.59, 5],
                'Meat Tornado': [1.59, 5],
                'A Literal Garden': [1.59, 5],
                'Chicken': [1.59, 5],
                'Sushi': [1.59, 5],
                'Burger': [1.59, 5],
                'Turf n Turf': [1.59, 5],
                'Turducken': [1.59, 5],
                'Quail': [1.59, 5]
                },
    'desserts': {'Ice Cream': [1.59, 5],
                 'Cake': [1.59, 5],
                 'Pie': [1.59, 5],
                 'Froyo': [1.59, 5],
                 'Flan': [1.59, 5],
                 'Creme Brulee': [1.59, 5],
                 'Chocolate Mousse': [1.59, 5],
                 'Chocolate Moose': [1.59, 5],
                 'Chocolate Mouse': [1.59, 5],
                 },
    'drinks': {'Coffee': [1.59, 5],
               'Tea': [1.59, 5],
               'Blood Of The Innocent': [1.59, 5],
               'Water': [1.59, 5],
               'Beer': [1.59, 5],
               'A Larger Beer': [1.59, 5],
               'Bubble Tea': [1.59, 5],
               'Faygo': [1.59, 5],
               'Red Bull': [1.59, 5],
               },
    'sides': {'Tiny Salad': [1.59, 5],
              'Cup Soap': [1.59, 5],
              'Fruit Bowl': [1.59, 5],
              'Fried Okra': [1.59, 5],
              'Bacon': [1.59, 5],
              'Giant Beer': [1.59, 5],
              'Just Carbs': [1.59, 5],
              'Potato Volcano': [1.59, 5],
              'Carrots': [1.59, 5]
              }
}
current = Order()

# Write menu to csv file

# with open('receipt.txt', 'w') as receipt_file:
#     csv_menu = csv.writer(csv_file, delimiter=',')
#     for category in menu_two:
#         for item in menu_two[category]:
#             csv_menu.writerow([category, item, menu_two[category][item]])
# menu_two = {}


class Order:
    def __init__(self):
        self.receipt = {'subtotal': 0}
        self.id = uuid.uuid4()

    def __repr__(self):
        return 'Order {} | Items: {} | Total: {}'.format(self.id, self.receipt['subtotal'], len(self.receipt))

    def __len__(self):
        return len(self.receipt)

    def add_item(self, item, quantity):
        try:
            flag = False
            for key, value in menu.items():
                if item in menu[key]:
                    flag = True
                    stock = menu[key][item][1]
                    if quantity < float(stock):
                        menu[key][item][1] -= 1
                        if item in current.receipt:
                            current.receipt[item] += quantity
                            total = _get_subtotal(item)
                            print(f'{current.receipt[item]} orders of {item} have been added to your meal. Your total is ${total}')
                        else:
                            current.receipt[item] = 1
                            total = _get_subtotal(item)
                            print(f'{quantity} order of {item} has been added to your meal. Your total is ${total}')
                    else:
                        print('We don\'t have that many in stock!')
            if flag is False:
                print('That\'s not on the menu!')
        except (TypeError, KeyError):
            print('Your input was invalid! Please order off the menu.')

    def remove_item(self, item, quantity):
        """
        This function handles removing items from the order.
        """
        for key, value in menu.items():
            if item in menu[key]:
                if current.receipt[item] == 1:
                    current.receipt['subtotal'] -= menu[key][item][0]
                    del current.receipt[item]
                else:
                    current.receipt[item] -= quantity
                    current.receipt['subtotal'] -= menu[key][item][0] * quantity
                total = round(current.receipt['subtotal'], 2)
                print(f'{quantity} order(s) of {item} has been removed from your meal. Your total is ${total}')

    def display_order(self, receipt):
        """
        This function prints the final receipt.
        """
        tax = round(_get_sales_tax(current.receipt['subtotal']), 2)
        print('*' * 50)
        print('The Snakes Cafe')
        print('"Eatability Counts"')
        print('Order', current.id)
        print('=' * 50)
        for key, value in current.receipt.items():
            unit_cost = _calculate_line_item(key)
            if unit_cost is not None:
                print(unit_cost[0].ljust(40), '$', unit_cost[1] * current.receipt[key])
        print('-' * 50)
        print('Subtotal'.ljust(40), '$', round(current.receipt['subtotal'], 2))
        print('Sales Tax'.ljust(40), '$', tax)
        print('-' * 10)
        print('Total Due'.ljust(40), '$', str(float(round(current.receipt['subtotal'] + tax))), 2)
        print('*' * 50)


def _import_menu(file_path):
    try:
        with open(file_path, 'r') as f:
            menu_import = csv.reader(f)
            for row in menu_import:
                item = iter(row[1:])
                # import pdb; pdb.set_trace()
                if row[0] in menu.keys():
                    menu[row[0]].update(dict(zip(item, item)))
                else:
                    menu[row[0]] = dict(zip(item, item))
            print_all(menu)
    except (IndexError, FileNotFoundError) as error:
        print('File not found or incorrect filetype; please use a .csv')
        what_menu()


def what_menu():
    print('***************************************')
    print('**    Welcome to the Snakes Cafe!    **')
    print('**    Please see our menu below.     **')
    print('**                                   **')
    print('**  To quit at any time, type "quit" **')
    print('***************************************')
    print('Would you like to import a menu?')
    menu_choice = input('> ')
    try:
        if menu_choice.lower() == 'yes':
            print('What is the filepath?')
            filepath = input('> ')
            _import_menu(filepath)
        else:
            global menu
            menu = default_menu
            print_all(menu)
    except TypeError:
        print('invalid input. Enter yes or no.')


def print_specific(order):
    try:
        print(order.title())
        print('-' * 8)
        for key, value in menu[order].items():
            print(key.ljust(50), '$' + str(value[0]))
        print('\n')
    except (TypeError, KeyError, IndexError):
        print('Oops! Something was wrong with your menu request.')


def print_all(dict):
    try:
        for key, value in dict.items():
            print(key.title())
            print('-' * 8)
            for key, value in dict[key].items():
                print(key.ljust(50), '$' + str(value[0]))
            print('\n')
        print('*' * 39)
        print('**   What would you like to order?   **')
        print('*' * 39)
    except KeyError:
        print('Oops! Something was wrong with your request.')


def _get_subtotal(item):
    """
    This function gets the subtotal of all purchased items.
    """
    try:
        for key, value in menu.items():
            if item in menu[key]:
                current.receipt['subtotal'] += menu[key][item][0]
        return round(current.receipt['subtotal'], 2)
    except TypeError:
        print('You managed to get something that isn\'t a number! What happened?')


def _get_sales_tax(subtotal):
    """
    This function calculates sales tax.
    """
    tax = subtotal * 0.101
    return tax


def _split_order(order, callback):
    if order[0] == 'Remove':
        order = order[1:]

    if not order[-1].isdigit():
        order.append(1)

    item = ' '.join(order[:-1])
    quant = int(order[-1])
    callback(item, quant)


def _calculate_line_item(item):
    """
    This function gets each line item and its cost.
    """
    for key, value in menu.items():
        if item in menu[key]:
            unit_cost = menu[key][item][0]
            item_name = item
            return(item_name, unit_cost)


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
            print_all(menu)

        elif order in categories:
            print_specific(order)

        elif order == 'display_order()':
            current.display_order(current.receipt)

        elif order == 'print()':
            current.display_order(current.receipt)

        elif order.split(' ').pop(0) == 'remove':
            print(order)
            _split_order(order.title().split(' '), current.remove_item)

        else:
            _split_order((order.title().split(' ')), current.add_item)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Thanks for your order!')
