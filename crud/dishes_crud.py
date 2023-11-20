import requests
from . import products_crud
from config import NOTION_TOKEN

DATABASE_ID = "824e9af0994249ada04f33dc9e73311f"
url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


async def get_dishes():
    payload = {"page_size": 100}
    response = requests.post(url=url, json=payload, headers=headers)

    data = response.json()
    result = data["results"]

    return result


async def get_available_dishes():

    available_dishes = []

    available_products = await products_crud.get_available_products()
    all_dishes = await get_dishes()

    available_products_ids = []
    for index in range(len(available_products['results'])):
        item = available_products['results'][index]['id']
        available_products_ids.append(item)

    for dish in all_dishes:
        match_counter = 0

        for product in available_products_ids:
            if {'id': product} in dish['properties']['Products']['relation']:
                match_counter += 1

        if match_counter == len(dish['properties']['Products']['relation']):
            available_dishes.append({
                'Dish name': dish['properties']['Dish']['title'][0]['plain_text'],
                'id': dish['id']

            })

    return available_dishes


async def get_marked_dishes():
    filter_condition = {
        "property": "Want to cook",
        "checkbox": {
            "equals": True
        }
    }
    params = {
        "filter": filter_condition
    }

    response = requests.post(url=url, json=params, headers=headers)

    result = response.json()

    items = list(item['properties']['Products']['relation'] for item in result['results'])

    return items


async def get_related_products(related_ids):
    related_objects = []

    for relation_id in related_ids:
        get_url = f"https://api.notion.com/v1/blocks/{relation_id}"
        response = requests.get(get_url, headers=headers)

        if response.status_code == 200:
            related_object = response.json()
            related_objects.append(related_object['child_page']['title'])

    return related_objects
