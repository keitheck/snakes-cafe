import uuid


menu = {
    'apps': {'Wings': 1.59,
             'Cookies': 1.59,
             'Spring Rolls': 1.59,
             'Fries': 1.59,
             'Pickles': 1.59,
             'Onion Rings': 1.59
             },
    'entrees': {'Salmon': 1.59,
                'Steak': 1.59,
                'Meat Tornado': 1.59,
                'A Literal Garden': 1.59,
                'Chicken': 1.59,
                'Sushi': 1.59,
                'Burger': 1.59
                },
    'desserts': {'Ice Cream': 1.59,
                 'Cake': 1.59,
                 'Pie': 1.59,
                 'Froyo': 1.59,
                 'Flan': 1.59,
                 'Creme Brulee': 1.59
                 },
    'drinks': {'Coffee': 1.59,
               'Tea': 2.59,
               'Blood Of The Innocent': 1.59,
               'Water': 1.59,
               'Beer': 1.59,
               'A Larger Beer': 1.59
               },
    'sides': {'Tiny Salad': 1.59,
              'Cup Soap': 1.59,
              'Fruit Bowl': 1.59,
              'Fried Okra': 1.59,
              'Bacon': 1.59,
              'Giant Beer': 1.59
              }
}

receipt = {'subtotal': 0,
           'order_id': uuid.uuid4().hex
           }

subtotal = 0


def print_welcome():
        print('***************************************')
        print('**    Welcome to the Snakes Cafe!    **')
        print('**    Please see our menu below.     **')
        print('**                                   **')
        print('**  To quit at any time, type "quit" **')
        print('***************************************')


def print_apps():
    print('Appetizers')
    print('-' * 8)
    for key, value in menu['apps'].items():
        print(key.ljust(50), '$' + str(value))
    print('\n')


def print_entrees():
    print('Entrees')
    print('-' * 8)
    for key, value in menu['entrees'].items():
        print(key.ljust(50), '$' + str(value))
    print('\n')


def print_sides():
    print('Sides')
    print('-' * 8)
    for key, value in menu['sides'].items():
        print(key.ljust(50), '$' + str(value))
    print('\n')


def print_desserts():
    print('Desserts')
    print('-' * 8)
    for key, value in menu['desserts'].items():
        print(key.ljust(50), '$' + str(value))
    print('\n')


def print_drinks():
    print('Drinks')
    print('-' * 8)
    for key, value in menu['drinks'].items():
        print(key.ljust(50), '$' + str(value))
    print('\n')


def print_what_to_order():
    print('***************************************')
    print('**   What would you like to order?   **')
    print('***************************************')


def print_menu():
    print_apps()
    print_entrees()
    print_sides()
    print_desserts()
    print_drinks()
    print_what_to_order()


def get_subtotal(order):
    for key, value in menu.items():
        if order in menu[key]:
            receipt['subtotal'] += menu[key][order]
    return round(receipt['subtotal'], 2)


def get_sales_tax(subtotal):
    tax = subtotal * 0.101
    return tax

def item_added(order):
    if order in receipt:
        receipt[order] += 1
        total = get_subtotal(order)
        print(f'{receipt[order]} orders of {order} have been added to your meal. Your total is ${total}')
    else:
        receipt[order] = 1
        total = get_subtotal(order)
        print(f'One order of {order} has been added to your meal. Your total is ${total}')


def remove_item(order):
    delete_item = order.split(' ')
    delete_item = ' '.join(delete_item[1:])
    for key, value in menu.items():
        if delete_item in menu[key]:
            receipt['subtotal'] -= menu[key][delete_item]
            if receipt[delete_item] == 1:
                del receipt[delete_item]
            else:
                receipt[delete_item] -= 1   
            total = receipt['subtotal']
            print(f'One order of {delete_item} has been removed from your meal. Your total is ${total}')


def print_receipt(receipt):
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
    print('Total Due'.ljust(40), '$', str(receipt['subtotal'] + tax))
    print('*' * 50)


def calculate_line_item(item):
    for key, value in menu.items():
        if item in menu[key]:
            unit_cost = menu[key][item]
            item_name = item
            return(item_name, unit_cost)


print_menu()

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
        print_what_to_order()  

    elif order == 'entrees':
        print('\n')
        print_entrees()
        print_what_to_order()

    elif order == 'sides':
        print('\n')
        print_sides()
        print_what_to_order()

    elif order == 'desserts':
        print('\n')
        print_desserts()
        print_what_to_order()

    elif order == 'drinks':
        print('\n')
        print_drinks()
        print_what_to_order()   

    elif order == 'order':
        print_receipt(receipt)

    elif order.split(' ').pop(0) == 'remove':
        remove_item(order.title())

    else:
        item_added(order.title())
