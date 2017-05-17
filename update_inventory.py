# updating inventory screen

inventory = {'stamina' : 50, 'dollars' : 0, 'keys' : 0, 'revolver' : 0, 'bullets': 0}
added_items = []

def display_inventory(inventory):
    '''Count number of items'''

    number_of_items =(str(sum(inventory.values())))



# def add_to_inventory(inventory, added_items):
#     '''Adds to the inventory dictionary a list of items from added_items'''

#     for item in added_items:
#         if item in inventory:
#             inventory[item] += 1
#         else:
#             inventory[item] = 1

#     return inventory



def print_table(inventory):
    '''Print table with inventory items (unordered, descending order, ascending order)'''

    number_of_items =(str(sum(inventory.values())))
    max_string = 0

    for item in inventory.keys():
        if len(item) > max_string:
            max_string = len(item)
    print('\ncount'+' '*max_string+'item name\n'
            '-----'+'-'*max_string+'---------')

    if True:
        ordered_list = sorted(((value,key) for key,value in inventory.items()), reverse=True)

        for value, key in ordered_list:
            print("{:>4}          {:>4}".format(value, key))

    print('-----'+'-'*max_string+'---------')
    print ("You need $40 to next level: "+number_of_items)
    display_inventory(inventory)



def add_item_to_inventory(board, inventory, y_current_position, x_current_position):
    '''Updates inventory and remove gathered item from board''' 

    if board[y_current_position][x_current_position] == '🔑':
        inventory['keys'] += 1
        board[y_current_position][x_current_position] = ' '

    if board[y_current_position][x_current_position] == '🗲':
        inventory['stamina'] += 50
        board[y_current_position][x_current_position] = ' '

    if board[y_current_position][x_current_position] == '💰':
        inventory['dollars'] += 10
        board[y_current_position][x_current_position] = ' '

    if board[y_current_position][x_current_position] == '🔫':
        inventory['revolver'] += 1
        board[y_current_position][x_current_position] = ' '

    if board[y_current_position][x_current_position] == '⁌':
        inventory['bullets'] += 1
        board[y_current_position][x_current_position] = ' '