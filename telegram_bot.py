import telebot
import config


bot = telebot.TeleBot(config.token)

#@bot.message_handler(commands=['start'])
#def start_message(message):
#   bot.send_message(message.chat.id, 'Пламенно зигую 0/0/0/!!!')

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)
#def send_text(message):
    #if message.text.lower() == 'зигую':
    #    bot.send_message(message.chat.id, 'Привет, мой создатель!')
    #elif message.text.lower() == 'пока':
    #    bot.send_message(message.chat.id, 'Прощай, создатель!')


if __name__ == '__main__':
    bot.polling(none_stop=True)
