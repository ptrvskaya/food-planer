import requests
from config import NOTION_TOKEN

NOTION_TOKEN = NOTION_TOKEN
DATABASE_ID = "06128957a2674355b17cacb595990322"
url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


async def get_products():
    payload = {"page_size": 100}
    response = requests.post(url=url, json=payload, headers=headers)

    data = response.json()
    result = data["results"]

    return result


async def get_available_products():
    filter_condition = {
        "property": "Available",
        "checkbox": {
            "equals": True
        }
    }
    params = {
        "filter": filter_condition
    }

    response = requests.post(url=url, json=params, headers=headers)

    result = response.json()

    return result



