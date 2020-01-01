import telebot


bot = telebot.TeleBot('911691979:AAGC8lyqXV-Sdwq58t6h2SWEpiGpI41fhso')

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Пламенно зигую 0/0/0/!!!')

@bot.message_handler(content_types=['text'])
def send_text(message):
	if message.text.lower() == 'зигую':
		bot.send_message(message.chat.id, 'Привет, мой создатель!')
	elif message.text.lower() == 'пока':
		bot.send_message(message.chat.id, 'Прощай, создатель!')

bot.polling()
