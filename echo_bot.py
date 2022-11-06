import telebot

bot = telebot.TeleBot("5644313050:AAFtg70_fPz-qyr2hQfJ7TXrlrUuxeo03F0", parse_mode=None)
@bot.message_handler(commands=['start', 'help'])
def  start(message):
	bot.send_message(message.chat.id , "Howdy, how are you doing?")
s
def custom_sender(method, url, **kwargs):
    print("custom_sender. method: {}, url: {}, params: {}".format(method, url, kwargs.get("params")))
    result = util.CustomRequestResponse('{"ok":true,"result":{"message_id": 1, "date": 1, "chat": {"id": 1, "type": "private"}}}')
    return result

bot.polling(none_stop=True)