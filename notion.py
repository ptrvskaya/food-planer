import json
import requests
from config import NOTION_TOKEN


class NotionClient:

    def __init__(self, NOTION_TOKEN):
        self.DATABASE_ID = "17b317c535c44d3a881f9208684aa225"
        self.headers = {
            "Authorization": "Bearer " + NOTION_TOKEN,
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
        }

    async def create_list_of_dishes(self, data):
        create_url = "https://api.notion.com/v1/pages"

        data_for_upload = {
            "parent": {
                "database_id": self.DATABASE_ID
            },
            "properties": {
                "Dish name": {
                    "title": [
                        {
                            "text": {
                                "content": data['Dish name']
                            }
                        }
                    ]
                },
                "Data": {
                    "relation": [
                        {
                            "id": data['id']
                        },
                    ]
                }
            }
        }
        data_for_upload = json.dumps(data_for_upload)
        result = requests.post(create_url, headers=self.headers, data=data_for_upload)

        if result.status_code == 200:
            print('Successfully —', result.status_code)
        else:
            print(result.text)

        return result


class NotionShLClient:

    def __init__(self, NOTION_TOKEN):
        self.DATABASE_ID = "0a7b4421b5904cd6bbc1453d014ed5db"
        self.headers = {
            "Authorization": "Bearer " + NOTION_TOKEN,
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
        }

    async def create_shopping_list(self, data):
        create_url = "https://api.notion.com/v1/pages"

        data_for_upload = {
            "parent": {
                "database_id": self.DATABASE_ID
            },
            "properties": {
                "Name": {
                    "title": [
                        {
                            "text": {
                                "content": data
                            }
                        }
                    ]
                },
                "Tags": {
                    "multi_select": []
                }
            }
        }

        data_for_upload = json.dumps(data_for_upload)
        result = requests.post(create_url, headers=self.headers, data=data_for_upload)

        if result.status_code == 200:
            print('Successfully added to shopping list')
        else:
            print(result.text)

        return result
