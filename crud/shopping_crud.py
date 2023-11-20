from notion import NotionShLClient
from . import dishes_crud
from config import NOTION_TOKEN

import requests

DATABASE_ID = "0a7b4421b5904cd6bbc1453d014ed5db"
url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

client = NotionShLClient(NOTION_TOKEN)


async def get_shopping_list():
    payload = {"page_size": 100}
    response = requests.post(url=url, json=payload, headers=headers)

    data = response.json()
    result = data["results"]

    return result


async def create_shopping_list():
    items = await dishes_crud.get_marked_dishes()
    shopping_set = set()

    for items_list in items:
        list_ids = [item_id['id'] for item_id in items_list]
        list_ids = set(list_ids)
        shopping_set = shopping_set.union(list_ids)

    shopping_list = await dishes_crud.get_related_products(list(shopping_set))
    listed_items = await get_shopping_list()

    if listed_items:
        await delete_shopping_list()

    for item in shopping_list:
        await client.create_shopping_list(item)

    return shopping_set


async def delete_shopping_list():
    shopping_list_items = await get_shopping_list()
    items_ids = [result["id"] for result in shopping_list_items]

    for item in items_ids:
        delete_url = f"https://api.notion.com/v1/pages/{item}"

        payload = {"archived": True}
        result = requests.patch(delete_url, json=payload, headers=headers)

        if result.status_code == 200:
            print("Successfully deleted")
        else:
            print("Failed to delete")
            print(result.text)


async def serve_shopping_list():
    list_items = await get_shopping_list()
    new_list_items = []
    for item in list_items:
        new_list_items.append(item['properties']['Name']['title'][0]['plain_text'])

    n = '\n'
    return f'Shopping list:\n{n.join(str(item) for item in new_list_items)}'
