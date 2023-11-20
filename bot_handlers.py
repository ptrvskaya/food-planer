from aiogram import F
from crud import shopping_crud, planner_crud
from inline_bot.callback_data import MyCallback
from main import bot, dp
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from aiogram.filters import CommandStart
from inline_bot.buttons import choice_task


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('''
    Hello! 
    
    This food planner for Notion helps to organize your shopping lists and menu!"

    You can create lists of dishes you like and also list of products, mark the ones you have in the fridge, so the program will show you the list of dishes you can prepare right now.

    You also can mark some dishes in the list and get the shopping list with needed ingredients.
    ''',
                         reply_markup=choice_task)


@dp.callback_query((MyCallback.filter(F.task_name == "shopping_list")))
async def give_to_bot_shopping_list(query: CallbackQuery, callback_data: MyCallback):
    await query.answer('Fine')

    await query.message.answer('Preparing your shopping list! Please wait')
    await shopping_crud.create_shopping_list()

    shopping_list = await shopping_crud.serve_shopping_list()
    await query.message.answer(shopping_list)
    await query.message.answer('Here is your shopping list. \nNow you can add some items by your own '
                               '\nWrite Add ... to do it')


@dp.callback_query((MyCallback.filter(F.task_name == "dishes_list")))
async def give_to_bot_shopping_list(query: CallbackQuery, callback_data: MyCallback):
    await query.answer('Fine')
    await query.message.answer('Preparing your dishes list! Please wait')

    await planner_crud.create_properties()
    await query.message.answer(f'So you see what you can cook in your Notion!')


@dp.message()
async def message_handler(message: Message):
    if 'Add ' in message.text:
        shopping_list = await shopping_crud.serve_shopping_list()

        if shopping_list:
            shopping_list += f'\n{message.text[4:]}'
            await message.answer(shopping_list)
        else:
            await message.answer('You can not add items to the empty list. Please, create one')
    else:
        await message.answer('You need to white Add ... to add items in your shopping list')
