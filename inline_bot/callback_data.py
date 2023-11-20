from aiogram.filters.callback_data import CallbackData


class MyCallback(CallbackData, prefix="my"):
    task_name: str

