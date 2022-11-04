from aiogram.types import Message
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command, Text

from photos.photos_in_telegram import Photos
from loader import dp

help_text = '<b>Поиск отелей:</b>\n' \
            '/lowprice - Поиск отелей по возрастанию цены\n' \
            '/highprice - Поиск отелей по убыванию цены\n' \
            '/bestdeal - Поиск отелей с условиями: диапазон цен, максимальная удаленность от центра\n' \
            '\n<b>Ваши отели:</b>\n' \
            '/history - История поиска с найденными отелями\n' \
            '/favorites - Отели, добавленные в избранное\n' \
            '\n<b>Другие команды</b>\n' \
            '/start - Перезапуск бота\n' \
            '/help - Вывод данного сообщение\n' \
            '\n<b>Замечание:</b>\n' \
            'Поиск отелей в России временно не доступен\n' \
            '\n<b>Рекомендации:</b>\n' \
            'При возникновении ошибок:\n' \
            '1. Попробовать перезапустить бота, отправив /start\n' \
            '2. Если не помогает 1 пункт - запустить снова через 2-5 минут\n' \
            '3. В других случаях можно написать разработчику @mchavchek'


@dp.message_handler(Command('help'), state='*')
async def bot_help(message: Message):
    """Send the user a description of commands and other useful information"""

    await message.bot.send_photo(photo=Photos.help.value, chat_id=message.chat.id,
                                 caption=help_text, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text('Справка'), state='*')
async def bot_help_(message: Message):
    await bot_help(message=message)
