
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
               'Tea': 1.59,
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

receipt = {
}

def get_subtotal(order):
    subtotal = 0
    for key, value in 


def print_welcome():
        print('***************************************')
        print('**    Welcome to the Snakes Cafe!    **')
        print('**    Please see our menu below.     **')
        print('**                                   **')
        print('**  To quit at any time, type "quit" **')
        print('***************************************')


def print_menu():

    print('Appetizers')
    print('-' * 8)
    for key, value in menu['apps'].items():
        print(key.ljust(50), '$' + str(value))
    print('\n')

    print('Entrees')
    print('-' * 8)
    for key, value in menu['entrees'].items():
        print(key.ljust(50), '$' + str(value))
    print('\n')

    print('Sides')
    print('-' * 8)
    for key, value in menu['sides'].items():
        print(key.ljust(50), '$' + str(value))
    print('\n')

    print('Desserts')
    print('-' * 8)
    for key, value in menu['desserts'].items():
        print(key.ljust(50), '$' + str(value))
    print('\n')

    print('Drinks')
    print('-' * 8)
    for key, value in menu['drinks'].items():
        print(key.ljust(50), '$' + str(value))
    print('\n')

    print('***************************************')
    print('**   What would you like to order?   **')
    print('***************************************')


print_menu()


def item_added(order):
    if order in receipt:
        total = get_subtotal(receipt)
        print(f'{receipt[order]} orders of {order} have been added to your meal. Your total is ${total}')
    else:
        print(f'One order of {order} has been added to your meal.')


while True:
    order = input('> ')
    if order == 'quit':
        exit()

    if order == 'menu':
        print_menu()

    item_added(order.title())
