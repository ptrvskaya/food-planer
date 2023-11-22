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

add_or_delete = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Add item to list",
                callback_data=MyCallback(task_name="add").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Delete item from list",
                callback_data=MyCallback(task_name="delete").pack()
            )
        ]
    ]
)

add_delete_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Add item to list",
                callback_data=MyCallback(task_name="add").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Delete item from list",
                callback_data=MyCallback(task_name="delete").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Go to main menu",
                callback_data=MyCallback(task_name="menu").pack()
            )
        ]
    ]
)

to_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Go to main menu",
                callback_data=MyCallback(task_name="menu").pack()
            )
        ]
    ]
)


main_menu = InlineKeyboardMarkup(
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
        ],
        [
            InlineKeyboardButton(
                text="Get my shopping list",
                callback_data=MyCallback(task_name="get_shopping_list").pack()
            )
        ]
    ]
)
