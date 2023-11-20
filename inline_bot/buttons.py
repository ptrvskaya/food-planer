from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from inline_bot.callback_data import MyCallback

choice_task = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Create shopping list",
                callback_data=MyCallback(task_name="shopping_list").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Create dishes list",
                callback_data=MyCallback(task_name="dishes_list").pack()
            )
        ]
    ]
)
