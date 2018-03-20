

print('***************************************')
print('**    Welcome to the Snakes Cafe!    **')
print('**    Please see our menu below.     **')
print('**                                   **')
print('**  To quit at any time, type "quit" **')
print('***************************************')

apps = ['Wings', 'Cookies', 'Spring Rolls']
entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
desserts = ['Ice Cream', 'Cake', 'Pie']
drinks = ['Coffee', 'Tea', 'Blood of the Innocent']


print('Appetizers')
print('-'*8)
for item in apps:
    print(item)
print('\n')

print('Entrees')
print('-'*8)
for item in entrees:
    print(item) 
print('\n')

print('Desserts')
print('-'*8)
for item in desserts:
    print(item)       
print('\n')

print('Drinks')
print('-'*8)
for item in drinks:
    print(item)
print('\n')
print('***************************************')
print('**   What would you like to order?   **')
print('***************************************')


receipt = {
}

while True:
    order = input('> ')  
    if order == 'quit':
        exit()

    if order in receipt:
        receipt[order] += 1
        print(f'{receipt[order]} orders of {order} have been added to your meal.')
    else:    
        receipt[order] = 1
        print(f'one order of {order} has been added to your meal.')
