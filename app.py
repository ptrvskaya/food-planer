from fastapi import FastAPI
from crud import planner_crud, shopping_crud

app = FastAPI()


@app.post("/api/create_shopping_list")
async def handle_shopping_list_request(data: dict):

    response_data = data

    if response_data:
        print('got request')
        return await shopping_crud.create_shopping_list()


@app.post("/api/create_dishes_list")
async def handle_dishes_list_request(data: dict):

    response_data = data

    if response_data:
        return await planner_crud.create_properties()
