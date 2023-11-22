from crud import shopping_crud

shopping_list = ''


async def get_shopping_list():
    global shopping_list
    if not shopping_list:
        shopping_list = await shopping_crud.serve_shopping_list()
    return shopping_list


async def add_item(item):
    global shopping_list
    shopping_list = await get_shopping_list()
    shopping_list += f'\n{item}'
    return shopping_list


async def delete_item(item):
    global shopping_list
    shopping_list = await get_shopping_list()
    if item in shopping_list:
        print('got item')
        shopping_list = shopping_list.replace(f'\n{item}', '')
        return shopping_list
    else:
        return f'There is no {item} in your list'
