import json
with open('storeinventory.json') as f:
    inventory = json.load(f)

for i in inventory:
    print(i)
print('--')


def add_item():

    new_dict_block = \
        {"name": input('add name: '), "price": int(input('add price: ')), "in stock": int(input('add stock: '))}
    print(new_dict_block)
    inventory.append(new_dict_block)

    print(inventory)


def change_item():
    item = select_item()
    change = input('(change name(n)(change price (p))(change stock(s))')

    if change == 'n':
        change_name = input('change name: ')
        item['name'] = change_name
        print(item)

    if change == 'p':
        change_price = input('change price: ')
        item['price'] = int(change_price)
        print(item)

    if change == 's':
        change_stock = input('change stock')
        item['price'] = int(change_stock)
        print(item)




def remove_item():
    item = select_item()
    inventory.remove(item)
    print(inventory)


...


def select_item():
    names = []
    for i in inventory:
        names.append(i['name'])


    lista = [0, 1]      #placeholder list
    while len(lista) > 1:
        name_call = input('enter name: ')
        lista.clear()

        for name in names[0: len(names)]:
            if name_call[0: len(name_call)] == name[0: len(name_call)]:
                potential_item = name
                lista.append(potential_item)

        print(len(lista))
        print(lista)

    else:
        name = (names.index(lista[0][0: len(lista[0])]))
        return (inventory[name])


...


def user_call():

    stage1_call = input('Options: (Change Item(c)) (Add Item(a)) (Remove Item(r))(Save Changes(s)): ')

    if stage1_call.lower() == 'c':
        change_item()
        user_call()
    elif stage1_call.lower() == 'r':
        remove_item()
        user_call()
    elif stage1_call.lower() == 'a':
        add_item()
        user_call()
    elif stage1_call.lower() == 's':
        ...
    else:
        user_call()


user_call()


for i in inventory:
    print(i)
print('--')

with open('storeinventory.json.', 'w') as f:
    json.dump(inventory, f, indent=2)