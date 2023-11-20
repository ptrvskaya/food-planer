import requests
from notion import NotionClient
from crud import dishes_crud
from config import NOTION_TOKEN

DATABASE_ID = "17b317c535c44d3a881f9208684aa225"
url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

client = NotionClient(NOTION_TOKEN)


async def create_properties():
    listed_items = await get_planner_items()

    if listed_items:
        await delete_planner_items()

    data = await dishes_crud.get_available_dishes()

    for item in data:
        await client.create_list_of_dishes(item)


async def get_planner_items():
    payload = {"page_size": 100}
    response = requests.post(url=url, json=payload, headers=headers)

    data = response.json()
    result = data["results"]

    return result


async def delete_planner_items():
    planner_items = await get_planner_items()
    items_ids = [result["id"] for result in planner_items]

    for item in items_ids:
        delete_url = f"https://api.notion.com/v1/pages/{item}"

        payload = {"archived": True}
        result = requests.patch(delete_url, json=payload, headers=headers)

        if result.status_code == 200:
            print("Successfully deleted")
        else:
            print("Failed to delete")
            print(result.text)
