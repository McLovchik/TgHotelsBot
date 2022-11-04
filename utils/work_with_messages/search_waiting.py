from aiogram.types.message import Message

from utils.work_with_messages.delete_messages import delete_message


async def send_waiting_message(message: Message) -> tuple[Message, Message]:
    """
    Sends waiting messages (text and sticker) when bot requests to api.
    Returns sended messages to delete them in future
    """

    search_text_message = await message.answer('<i>Выполняю поиск...</i>')
    search_sticker_message = \
        await message.answer_sticker(sticker='CAACAgIAAxkBAAEGPdBjXOSiezHXCIYn3k_DU2Nx_khoVwAC6BUAAiMlyUtQqGgG1fAXAAEqBA')
    return search_text_message, search_sticker_message


async def del_waiting_messages(text: Message, sticker: Message):
    """Deletes waiting messages"""

    await delete_message(text)
    await delete_message(sticker)
