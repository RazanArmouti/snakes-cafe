menu = ['wings', 'cookies',
        'spring rolls', 'salmon',
        'steak', 'meat tornado',
        'a literal garden', 'ice Cream',
        'cake', 'pie', 'coffee',
        'tea', 'unicorn tears']
user_orders = []
last_orders = []


def ordering():

    order = input('>> ').lower()
    if order in menu:
        user_orders.append(order)
        if order not in last_orders:
            last_orders.append(order)
        print(
            f'** {user_orders.count(order)} order of {order} have been added to your meal **')
        ordering()

    elif order == 'quit':
        print('thank you \n your order will be ready soon \n Your order is:')
        for list_item in last_orders:
            print(f'{user_orders.count(list_item)} order of {list_item} ')
    elif order not in menu:
        print(
            f'sorry {order} your order is not in the menu :( \nPlease choose one of the menu items')
        ordering()
