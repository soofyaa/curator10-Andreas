import telebot

bot = telebot.TeleBot('6870956120:AAFaIBiYvbkSdSlv9VnbKlawhsZGTcw0F_o')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '*Приветствую!*', parse_mode='Markdown')


@bot.message_handler(commands=['stop'])
def main(message):
    bot.send_message(message.chat.id, '*До встречи!*', parse_mode='Markdown')


@bot.message_handler(commands=['menu'])
def main(message):
    bot.send_message(message.chat.id, 'Тут должно быть меню', parse_mode='Markdown')


@bot.message_handler(commands=['my_link'])
def main(message):
    bot.send_message(message.chat.id, 'Это [ССЫЛКА](https://t.me/Andreasxwlnk)', parse_mode='Markdown')


@bot.message_handler(commands=['warning'])
def main(message):
    bot.send_message(message.chat.id, 'Сюда [НЕ НАЖИМАТЬ](https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley)', parse_mode='Markdown')



bot.infinity_polling()
