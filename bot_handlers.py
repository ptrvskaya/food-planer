import asyncio
from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from bot_FSM import MyFSMStates
from crud import shopping_crud, planner_crud
from inline_bot.callback_data import MyCallback
from main import bot, dp
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, StateFilter
from inline_bot.buttons import choice_task, add_or_delete, add_delete_menu, to_menu, main_menu
from bot_methods import add_item, delete_item, get_shopping_list
from aiogram.fsm.context import FSMContext

add_delete_router = Router()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Hello! *This food planner for Notion helps to organize your shopping lists and menu!* \n\nYou can *create lists of dishes* you like and also list of products, mark the ones you have in the fridge, so the program will show you the *list of dishes you can prepare* right now. \n\nYou also can mark some dishes in the list and *get the shopping list* with needed ingredients. \n\n*You can manage your data here:* \nhttps://shorturl.at/bgqsy',
                         parse_mode=ParseMode.MARKDOWN,
                         reply_markup=choice_task)


@dp.callback_query((MyCallback.filter(F.task_name == "shopping_list")))
async def give_to_bot_shopping_list(query: CallbackQuery, callback_data: MyCallback):
    await query.message.answer('Preparing your shopping list! \nIt can take up to 30 seconds. *Please wait*',
                               parse_mode=ParseMode.MARKDOWN)

    await shopping_crud.create_shopping_list()
    await asyncio.sleep(10)
    await query.message.answer('Almost there!')
    shopping_list = await shopping_crud.serve_shopping_list()

    await query.message.answer(f'*Shopping list:*\n{shopping_list}', parse_mode=ParseMode.MARKDOWN)
    await query.message.answer('Here is your shopping list. \nNow you can *add or delete* some items by your own',
                               parse_mode=ParseMode.MARKDOWN,
                               reply_markup=add_or_delete)


@dp.callback_query((MyCallback.filter(F.task_name == "dishes_list")))
async def give_to_bot_shopping_list(query: CallbackQuery, callback_data: MyCallback):
    await query.message.answer('Preparing your dishes list! *Please wait*', parse_mode=ParseMode.MARKDOWN)

    await planner_crud.create_properties()
    await query.message.answer('*Your menu is ready!* \n\nYou see what you can cook in your Notion! \nhttps://shorturl.at/apEU4',
                               parse_mode=ParseMode.MARKDOWN,
                               reply_markup=to_menu)


@dp.callback_query((MyCallback.filter(F.task_name == "add")))
@add_delete_router.message(StateFilter(None))
async def add_item_handler(query: CallbackQuery, callback_data: MyCallback, state: FSMContext):
    await query.message.answer('Please send a name of item you want to add')
    await state.set_state(MyFSMStates.ADD)


@dp.callback_query((MyCallback.filter(F.task_name == "delete")))
@add_delete_router.message(StateFilter(None))
async def delete_item_handler(query: CallbackQuery, callback_data: MyCallback, state: FSMContext):
    await query.message.answer('Please send a name of item you want to delete')
    await state.set_state(MyFSMStates.DELETE)


@dp.message()
async def add_delete_handler(message: Message, state: FSMContext):

    current_state = await state.get_state()
    item = message.text

    if current_state == MyFSMStates.ADD:
        shopping_list = await add_item(item=item)
        await message.answer(shopping_list)
        await message.answer('Do you want to change anything else?', reply_markup=add_delete_menu)
    elif current_state == MyFSMStates.DELETE:
        shopping_list = await delete_item(item=item)
        await message.answer(shopping_list)
        await message.answer('Do you want to change anything else?', reply_markup=add_delete_menu)
    else:
        await message.answer('What do you want to do?', reply_markup=add_delete_menu)


@dp.callback_query((MyCallback.filter(F.task_name == "menu")))
async def menu(query: CallbackQuery, callback_data: MyCallback):
    await query.message.answer('*Welcome to main menu!* \nHere you can create your menu, generate your shopping list or get the existing one',
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=main_menu
    )


@dp.callback_query((MyCallback.filter(F.task_name == "get_shopping_list")))
async def get_list(query: CallbackQuery, callback_data: MyCallback):
    shopping_list = await get_shopping_list()
    await query.message.answer(shopping_list, reply_markup=to_menu)